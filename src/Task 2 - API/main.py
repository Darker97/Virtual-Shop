import atexit
import flask as Flask



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
# API logic

def QuestionToTheServer():
    if CanHeDoThat():
        return
    else:
        return "Error 413 - Data Forbidden"

def NewData():
    if CanHeDoThat():
        return
    else:
        return "Error 413 - Data Forbidden"

def NewUser():
    if CanHeDoThat():
        return
    else:
        return "Error 413 - No Admin"

def Login():
    if CanHeDoThat():
        return
    else:
        return "Error 413 - Not a User"

# ------------------------------------------
# API
def startAPI():
    app = Flask("API")
    @app.route('/')
    def index():
        return """ The Most efficient way to Optimize an SQL Query is to eliminate it.  """

    @app.route('/Data', methods=['GET'])
    def platzhalter():
        return QuestionToTheServer()

    @app.route('/Data', methods=['POST'])
    def platzhalter():
        return NewData()

    @app.route('/User', methods=['GET'])
    def platzhalter():
        return Login()

    @app.route('/User', methods=['POST'])
    def platzhalter():
        return NewUser()


    app.run(debug=True)


# ------------------------------------------
# Check for credentials
def CanHeDoThat():
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