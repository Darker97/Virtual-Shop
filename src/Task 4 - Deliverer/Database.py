import mysql.connector as mysql
import time

# connects to the DB
class Database:
    def ConnectToDatabase(self) -> Database:
        try:
            data = Database()
            if data.is_connected():
                print("Connection Established!!!")
                print("------------------------------------------------------")
                return data
            
        except Exception as e:
            print(e)
            print("...")
            time.sleep(30)
            print("Trying again")
            print("------------------------------------------------------")
            ConnectToDatabase()


    # connects to the Database and return the Connection
    def Database(self) -> Database:
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
            database=database
        )
        return Database

    # Gets a Query, sends it to the DB and returns the answer
    def SendQuery(self, Database, Query) -> answer:
        pointer = Database.cursor()

        pointer.execute(Query)

        answer = pointer.fetchall()

        return answer