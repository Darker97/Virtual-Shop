import gpg as gpg
import flask as Flask
from flask import request
from flask import Flask
import datetime

import GPG_Functions
import Database_Functions

# all api Functions
def startApi(db, key):
    print("Starting API")

    app = Flask("SecApi")
    @app.route('/')
    def index():
        return("But I need to protect the humans.")

    @app.route('/chaos')
    def Chaos():
        return "LEAVE_ME_HERE.readme"

    @app.route('/LEAVE_ME_HERE.readme')
    def Leave():
        return "FSOCIETY.dat"

    # Checks if the User is there and sends a Token
    @app.route('/security/login')
    def login():
        User = request.form['User']
        Password = request.form['Password']
        if isThisAUser(db,User,Password):
            Token = User + "-----|------" +  Password + "-----|------" + datetime.datetime.now(datetime.timezone.utc)
            # sign with public
            Token = GPG_Functions.sign(gpg.export_keys(key), Token)
            # encrypt with private
            Token = GPG_Functions.Encryptor(gpg.export_key(key,True), Token)
            return Token
        else:
            return "ERROR"

    # checks if its our Token
    @app.route('/securtiy/check')
    def check():
        Token = request.form['Token']

        # Decrypt with public
        Token = GPG_Functions.Decryptor(gpg.export_keys(key), Token)#
        # verify with privat
        return GPG_Functions.verify(gpg.export_key(key,True), Token)

    # Checks if the given question contains a Word that leds to SQL Injections.
    @app.route('/security/injection')
    def checkForInjection():
        question = request.form['question']

        File = open("InjectionList.txt")
        WordList = File.readlines()

        for Word in WordList:
            if Word in question:
                return False
        
        return True

    app.run(debug=True)


# Is the given User Valid?
def isThisAUser(Database, User, Password):
    pointer = Database.cursor()

    Query = ""

    FinalQuery = (Query, (User, Password))
    pointer.execute(FinalQuery)

    if pointer.fetchall().count > 0:
        return True
    else:
        return False



# ---------------------------------------------------------------------


print("""
   _____                      _ __           ___    ____  ____
  / ___/___  _______  _______(_) /___  __   /   |  / __ \/  _/
  \__ \/ _ \/ ___/ / / / ___/ / __/ / / /  / /| | / /_/ // /  
 ___/ /  __/ /__/ /_/ / /  / / /_/ /_/ /  / ___ |/ ____// /   
/____/\___/\___/\__,_/_/  /_/\__/\__, /  /_/  |_/_/   /___/   
                                /____/                        
""")

print("------------------------------------------")
print("Creating new Keys and connecting to Database")
print("\n")
key = GPG_Functions.createKeys()
DB = Database_Functions.ConnectToDatabase()
print("------------------------------------------")
print("\n")
startApi(DB, key)