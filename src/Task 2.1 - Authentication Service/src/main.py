from flask import request
from flask import Flask
import datetime
import json

from GPG_Functions import GPG_Functions
from Database_Functions import Database_Functions

# all api Functions
def startApi(db, privatekey , publickey):
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
    @app.route('/security/login', methods=['GET'])
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

            # encrypt with private
            Token = GPG_Functions.Encryptor( privatekey, Token)

            return Token
        else:
            return "ERROR"

    # checks if its our Token and returns the role if yes.
    @app.route('/securtiy/check', methods=['GET'])
    def check():
        Token = request.form['Token']

        # Decrypt with public
        Token = GPG_Functions.Decryptor( publickey, Token)

        try:
            return Token["Role"]
        except Exception as e:
            return "False"
            

    # Checks if the given question contains a Word that leds to SQL Injections.
    @app.route('/security/injection', methods=['GET'])
    def checkForInjection():
        question = request.form['question']

        File = open("./src/InjectionList.txt")
        WordList = File.readlines()

        for Word in WordList:
            if Word in question:
                return "False"
        
        return "True"

    @app.errorhandler(404)
    def not_found(error):
        return "Error 404 - failed successfully"

    app.run(debug=True, host='0.0.0.0')


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
privatekey , publickey = GPG_Functions.createKeys()
DB = Database_Functions.ConnectToDatabase()
print("------------------------------------------")
print("\n")
startApi(DB, privatekey , publickey)