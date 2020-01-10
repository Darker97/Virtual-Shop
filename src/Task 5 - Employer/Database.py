import mysql.connector as mysql
import time

# connects to the DB
class Database:
    def ConnectToDatabase():
        try:
            data = Database.Database()
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
            Database.ConnectToDatabase()


    # connects to the Database and return the Connection
    def Database():
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
    def SendQuery( Database, Query):
        pointer = Database.cursor()
        pointer.execute(Query)
        Database.commit()

        answer = pointer.fetchall()

        return str(answer)