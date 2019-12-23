import json
import mysql.connector as mysql
import time
import socket

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


def queryLoader(Connection):
    print("Starting to load Data")
    File = open("query.sql")
    Querys = File.readlines()
    for aciton in Querys:
        Connection.execute(aciton)



# Checks if the Connection is established. If not, we wait.
def startFile():
    time.sleep(10)

    print("""  
  _______    _     _       _____                _            
 |__   __|  | |   | |     / ____|              | |           
    | | __ _| |__ | | ___| |     _ __ ___  __ _| |_ ___ _ __ 
    | |/ _` | '_ \| |/ _ \ |    | '__/ _ \/ _` | __/ _ \ '__|
    | | (_| | |_) | |  __/ |____| | |  __/ (_| | ||  __/ |   
    |_|\__,_|_.__/|_|\___|\_____|_|  \___|\__,_|\__\___|_|   """)

    try:
        data = connection()
        if data.is_connected():
            queryLoader(data.cursor())
            print("------------------------------------------------------")
            print("Tables Are Created!!!")
            print("------------------------------------------------------")
    except Exception as e:
        print("------------------------------------------------------")
        print(e)
        print("Proceeding...")
        time.sleep(30)
        print("Trying again")
        print("------------------------------------------------------")
        startFile()

# ------------------------------------------------ #

startFile()