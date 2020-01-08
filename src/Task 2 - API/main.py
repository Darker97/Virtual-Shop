import atexit
import time
import mysql.connector as mysql

from flask import Flask
from flask import request

from ApiLogic import ApiLogic
from BotLogic import BotLogic
from Database_Functions import Database_Functions

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
    app = Flask("Api")

    query = ApiLogic.queryloader()

    @app.route('/')
    def index():
        return """ The Most efficient way to Optimize an SQL Query is to eliminate it.  """

    # Question with QuestionID
    @app.route('/Data', methods=['GET'])
    def QuestionWithID():
        print("GET DATA Request")
        return ApiLogic.QuestionToTheServer(request.form['SecurityCookie'], request.form['QuestionID'], Database, query)

    # Question with own Script
    @app.route('/Data/Special', methods=['GET'])
    def QuestionWithoutID():
        return ApiLogic.SpecialQuestionToTheServer(request.form['SecurityCookie'], request.form['Data'], request.form['QuestionID'], Database, query)

    # Login
    @app.route('/User', methods=['GET'])
    def Login():
        print("GET USER Request")
        return ApiLogic.Login(request.form['Password'], request.form['UserName'], Database, query)

    # Bought
    @app.route('/Product', methods=['GET'])
    def ProductBought():
        return ApiLogic.ProductBought(request.form['SecurityCookie'], request.form['DATA'], Database)

    # Delivered
    @app.route('/Product', methods=['POST'])
    def ProductDelivered():
        return ApiLogic.Productdeliverd(request.form['SecurityCookie'], request.form['Data'], Database)

    #review
    @app.route('/review', methods=['GET'])
    def ReviewMade():
        return ApiLogic.Review(request.form['SecurityCookie'], request.form['Product'], request.form['Review'], Database)

    @app.errorhandler(404)
    def not_found(error):
        return "Error 404 - I'm a Teapot"

    app.run(debug=True, host='0.0.0.0')


# ------------------------------------------

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
DB = Database_Functions.ConnectToDatabase()
setup()
startAPI(DB)