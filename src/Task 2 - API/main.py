import atexit
import time
import mysql.connector as mysql

import flask as Flask
from flask import request

import ApiLogic
import BotLogic
import Database

# ------------------------------------------

# setup for the tool
def setup():
    atexit.register(exit)
    BotLogic.BotStart("Hello")

# Exit function that gets called when the Tool is closed
def exit():
    BotLogic.BotExit("Good Bye")

# ------------------------------------------
# API - The Paths of the API
def startAPI(Database):
    app = Flask("API")

    query = ApiLogic.queryloader()

    @app.route('/')
    def index():
        return """ The Most efficient way to Optimize an SQL Query is to eliminate it.  """

    @app.route('/Data', methods=['GET'])
    def platzhalter():
        print("GET DATA Request")
        return ApiLogic.QuestionToTheServer(request.form['SecurityCookie'], request.form['QuestionID'], Database, query)

    @app.route('/Data/Special', mehods=['GET'])
    def platzhalter():
        print("Special DATA GET REQUEST")
        return ApiLogic.SpecialQuestionToTheServer(request.form['SecurityCookie'], request.form['Data'], request.form['QuestionID'], Database, query)

    @app.route('/Data', methods=['POST'])
    def platzhalter():
        print("POST DATA Request")
        return ApiLogic.NewData(request.form['SecurityCookie'],request.form['Data'],request.form['DataID'], Database, query)

    @app.route('/User', methods=['GET'])
    def platzhalter():
        print("GET USER Request")
        return ApiLogic.Login(request.form['Password'], request.form['UserName'], Database, query)

    @app.route('/User', methods=['POST'])
    def platzhalter():
        print("GET USER Request")
        return ApiLogic.NewUser(request.form['SecurityCookie'], request.form['Data'], Database, query)


    @app.errorhandler(404)
    def not_found(error):
        return "Error 404 - I'm a Teapot"

    app.run(debug=True)


# ------------------------------------------
# Control of the Process
# Will connect to the DB and then start the API
def main():
    print("""
             _____ _                    ___  ______ _____ 
            /  ___| |                  / _ \ | ___ \_   _|
            \ `--.| |__   ___  _ __   / /_\ \| |_/ / | |  
             `--. \ '_ \ / _ \| '_ \  |  _  ||  __/  | |  
            /\__/ / | | | (_) | |_) | | | | || |    _| |_ 
            \____/|_| |_|\___/| .__/  \_| |_/\_|    \___/ 
                              | |                         
                              |_|                         
    """)

    try:
        DB = Database.connection()
        if DB.is_connected():
            print("Connected to Database!!!")
            print("Proceeding")
            print("------------------------------------------------------")
            print("\n")
            startAPI(DB)
    except Exception as e:
        print("------------------------------------------------------")
        print(e)
        print("Proceeding...")
        time.sleep(30)
        print("Trying again")
        print("------------------------------------------------------")
        main()

# ------------------------------------------

setup()
main()
