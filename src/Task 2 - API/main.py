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
        answer = ApiLogic.QuestionToTheServer(request.form['SecurityCookie'], request.form['QuestionID'], Database, query)
        return answer

    # Question with own Script
    @app.route('/Data/Special', methods=['GET'])
    def QuestionWithoutID():
        answer = ApiLogic.SpecialQuestionToTheServer(request.form['SecurityCookie'], request.form['Data'], request.form['QuestionID'], Database, query)
        return answer

    # Login
    @app.route('/User', methods=['GET'])
    def Login():
        answer = ApiLogic.Login(request.form['Password'], request.form['UserName'], Database, query)
        return answer

    # Bought
    @app.route('/Product', methods=['GET'])
    def ProductBought():
        answer = ApiLogic.ProductBought(request.form['SecurityCookie'], request.form['DATA'], Database)
        return answer

    # Delivered
    @app.route('/Product', methods=['POST'])
    def ProductDelivered():
        answer = ApiLogic.Productdeliverd(request.form['SecurityCookie'], request.form['Data'], Database)
        return answer

    #review
    @app.route('/review', methods=['GET'])
    def ReviewMade():
        answer = ApiLogic.Review(request.form['SecurityCookie'], request.form['Product'], request.form['Review'], Database)
        return answer

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