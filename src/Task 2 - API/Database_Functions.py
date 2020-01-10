import mysql.connector as mysql
import time

class Database_Functions:

    def ConnectToDatabase():
        try:
            data = Database_Functions.Database()
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
            Database_Functions.ConnectToDatabase()


    # connects to the Database
    def Database():
        File = open("Setup.config").readlines()
        host = File.pop(0)
        port = File.pop(0)
        user = File.pop(0)
        passwd = File.pop(0)
        databaseName = File.pop(0)

        print("------------------------------------------------------")
        print("Connecting to Database: " + host + " as " + user + " on port " + port)
        print("Password: " + passwd)
        print("------------------------------------------------------")

        DB = mysql.connect(
            host=host,
            port=port,
            user=user,
            database=databaseName
        )
        return DB