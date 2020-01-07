import json
import mysql.connector as mysql
import time
from tqdm import tqdm
import names
import hashlib
import random

# Establishes the Connection to the DB
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
            LoadingTables(data.cursor())
            print("------------------------------------------------------")
            print("Tables Are Created!!!")
            print("------------------------------------------------------")
            print("\n")
            print("Loading Data")
            
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

# Loads the Tables
def LoadingTables(Connection):
    File = open("./Querys/Table_query.sql")
    Querys = File.readlines()
    for action in tqdm(Querys, desc="Loading Tables"):
        Connection.execute(action)

# Loads the Products
def LoadingProducts(Connection):
    File = open ("./Querys/Product_DATA")
    Data = File.readlines()
    ID = 1

    insertQuery =  """INSERT INTO `Shop`.`Products` (`ID`, `Name`, `PrdouctNumber`, `Description`, `Calories`, `Protein`, `Fat`, `Sodium`, `Fiber`, `Carbo`, `Sugar`, `Vitamins`, `Price`) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    for data in tqdm(Data, desc="Loading Products"):
        decrypted = json.load(data)

        Name = str(decrypted["name"])
        ProductNumber = ID
        Description = ""
        Calories = str(decrypted["calories"])
        Protein = str(decrypted["protein"])
        Fat = str(decrypted["fat"])
        Sodium = str(decrypted["sodium"])
        Fiber = str(decrypted["fiber"])
        Carbo = str(decrypted["carbo"])
        Sugar = str(decrypted["sugars"])
        Vitamins = str(decrypted["vitamins"])
        Price = str(random.randint(1,10))

        FinalQuery = (insertQuery ,(ID, Name, ProductNumber, Description, Calories, Protein, Fat, Sodium, Fiber, Carbo, Sugar, Vitamins, Price))
        Connection.execute(FinalQuery)
        Connection.commit()

        ID += 1

# Loads random Customers
def LoadingCustomers(Connection):
    insertQuery =  """INSERT INTO `Shop`.`Customers` (`ID`, `Name`, `Surname`, `username`) 
                        VALUES (%s, %s, %s, %s);  """
    x = range(300)
    for i in tqdm(x, desc="Generating Users"):
        Name = names.get_first_name()
        surname = names.get_last_name()
        username = Name+surname

        FinalQuery = (insertQuery ,(i, Name, surname, username))
        Connection.execute(FinalQuery)
        Connection.commit()

# Loads pre-made Users
def LoadingUsers(Connection):
    file = open("Querys/UserData.json")
    strings = file.readlines()

    insertCustomerQuery =  """INSERT INTO `Shop`.`Customers` (`ID`, `Name`, `Surname`, `username`) 
                        VALUES (%s, %s, %s, %s);  """
    insertUserQuery = """INSERT INTO `Shop`.`User` (`USERID`, `ROLE`, `UserName_Hashed`, `Password_Hashed`, `Customers_ID`) 
                    VALUES (%s, %s, %s, %s, %s);  """

    for data in tqdm(strings, desc="Loading Users"):
        encoded = json.load(data)

        ID = str(encoded["Customers_ID"])
        Name = str(encoded["Name"])
        Surname = str(encoded["Surname"])
        USERID = str(encoded["USERID"])
        Role = str(encoded["ROLE"])
        UserName = str(encoded["UserName"])
        Password = str(encoded["Password"])
        Customers_ID = ID

        # UserName and Password need to be hashed!!!
        UserName = hashlib.sha3_256(UserName)
        Password = hashlib.sha3_256(Password)

        # Insert the Users into the Database
        Connection.execute(insertCustomerQuery, (ID, Name, Surname, UserName))
        Connection.execute(insertUserQuery, (USERID, Role, UserName, Password, Customers_ID))
