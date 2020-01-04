import gpg as gpg
import flask as Flask
from flask import request
from flask import Flask
import datetime
import json

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
        role = isThisAUser(db,User,Password)

        Timestamp = ""

        if isThisAUser(db,User,Password) != "False":
            Token = """ 
            { 
                "User" = "%s", 
                "password" = %s, 
                "Role"= %s, 
                "Timestamp" = %s 
            } """

            FinalToken = (Token, (User, Password, role, Timestamp))
            json.dumps(FinalToken)

            # sign with public
            Token = GPG_Functions.sign(gpg.export_keys(key), Token)
            # encrypt with private
            Token = GPG_Functions.Encryptor(gpg.export_key(key,True), Token)
            return Token
        else:
            return "ERROR"

    # checks if its our Token and returns the role if yes.
    @app.route('/securtiy/check')
    def check():
        Token = request.form['Token']

        # Decrypt with public
        Token = GPG_Functions.Decryptor(gpg.export_keys(key), Token)#
        # verify with privat
        if GPG_Functions.verify(gpg.export_key(key,True), Token):
            return Token["Role"]
        else:
            return "False"

    # Checks if the given question contains a Word that leds to SQL Injections.
    @app.route('/security/injection')
    def checkForInjection():
        question = request.form['question']

        File = open("InjectionList.txt")
        WordList = File.readlines()

        for Word in WordList:
            if Word in question:
                return "False"
        
        return "True"

    @app.errorhandler(404)
    def not_found(error):
        return "Error 404 - failed successfully"

    app.run(debug=True)


# Is the given User Valid?
def isThisAUser(Database, User, Password):
    pointer = Database.cursor()

    Query = "select ROLE from User where UserName_Hashed = %s and Password_Hashed = %s;"

    FinalQuery = (Query, (User, Password))
    pointer.execute(FinalQuery)

    answer = pointer.fetchall()

    if answer.count > 0:
         return answer
    else:
        return "False"



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