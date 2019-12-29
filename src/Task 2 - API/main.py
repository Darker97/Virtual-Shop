import atexit
import time
import mysql.connector as mysql

import flask as Flask
from flask import request



# ------------------------------------------

# setup for the tool
def setup():
    atexit.register(exit)
    BotStart("Hello")

# Exit function that gets called when the Tool is closed
def exit():
    BotExit("Good Bye")

def BotExit(Nachricht):
    # Beim Bot abmelden

def BotStart(Nachricht):
    # Beim Bot anmelden

# ------------------------------------------
# API logic - Erverything the API will do

def QuestionToTheServer(SecurityCookie, QuestionID):
    if CanHeDoThat():
        return
    else:
        return "Error 413 - Data Forbidden"

def NewData(SecurityCookie, Data, DataID):
    if CanHeDoThat():
        return
    else:
        return "Error 413 - Data Forbidden"

def NewUser(SecurityCookie, Data):
    if CanHeDoThat():
        return
    else:
        return "Error 413 - No Admin"

def Login(Password, UserName):
    try:
        return SecurityGiveUser()
    except:
        return "Error 413 - Not a User"

# ------------------------------------------
# API - The Paths of the API
def startAPI():
    app = Flask("API")

    @app.route('/')
    def index():
        return """ The Most efficient way to Optimize an SQL Query is to eliminate it.  """

    @app.route('/Data', methods=['GET'])
    def platzhalter():
        return QuestionToTheServer(request.form['SecurityCookie'], request.form['QuestionID'])

    @app.route('/Data', methods=['POST'])
    def platzhalter():
        return NewData(request.form['SecurityCookie'],request.form['Data'],request.form['DataID'])

    @app.route('/User', methods=['GET'])
    def platzhalter():
        return Login(request.form['Password'], request.form['UserName'])

    @app.route('/User', methods=['POST'])
    def platzhalter():
        return NewUser(request.form['SecurityCookie'], request.form['Data'])


    @app.errorhandler(404)
    def not_found(error):
        return "Error 404 - I'm a Teapot"

    app.run(debug=True)


# ------------------------------------------
# Check with the Security

def CanHeDoThat():
    pass
def SecurityGiveUser():
    pass

# ------------------------------------------
# Connection with Database
def connection():
    File = open("Setup.config").readlines()
    host = File.pop(0)
    port = File.pop(0)
    user = File.pop(0)
    passwd = File.pop(0)
    database = File.pop(0)

    print("------------------------------------------------------")
    print("Connecting to Database: " + host + " as " + user + " on port " + port)
    print("Password: " + passwd)
    print("------------------------------------------------------")

    Database = mysql.connect(
        host=host,
        port=port,
        user=user,
        # passwd=passwd,
        # unix_socket="../var/run/mysqld/mysqld.sock",
        database=database
        # auth_plugin='mysql_native_password'
    )
    return Database
# ------------------------------------------
# Control of the Process
# Will connect to the DB and then start the API
def main():
    try:
        Database = connection()
        if Database.is_connected():
            print("Connected to Database!!!")
            print("Proceeding")
            print("------------------------------------------------------")
            print("\n")
            startAPI()
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