import gpg
import mysql.connector as mysql


# ------------------------------------------
# Generates the keys we need

def createKeys():
    input_data = gpg.gen_key_input(key_type="RSA", key_length=1024)
    key = gpg.gen_key(input_data)

    exportKey = []
    # Public key
    exportKey.insert(0, gpg.export_keys(key))

    #Private Key
    exportKey.insert(1, gpg.export_keys(key, True))

    return exportKey


# all api Functions
def startApi():
    print("Starting API")



# ------------------------------------------
# connects to the Database
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
        # passwd=passwd,
        # unix_socket="../var/run/mysqld/mysqld.sock",
        database=database
        # auth_plugin='mysql_native_password'
    )
    return Database

# Is the given User Valid?
def isThisAUser(Database, User, Password):
    pointer = Database.cursor()

    Query = ""

    FinalQuery = (Query, (User, Password))
    pointer.execute(FinalQuery)

    if pointer.fetchall().count > 0:
        return True
    else:
        return False

# ------------------------------------------
def Encryptor(key, data):
    encrypted_data = gpg.encrypt(data, key)
    return str(encrypted_data)

def Decryptor(key, data):
    decrypted_data = gpg.decrypt(data, key)
    return str(decrypted_data)

def sign(key, data):
    signed_data = gpg.sign(data, key)
    return str(signed_data)

def verify(key, data):
    verified = gpg.verify(data, key)
    return str(verified)
# ------------------------------------------

# ------------------------------------------
print("""
   _____                      _ __           ___    ____  ____
  / ___/___  _______  _______(_) /___  __   /   |  / __ \/  _/
  \__ \/ _ \/ ___/ / / / ___/ / __/ / / /  / /| | / /_/ // /  
 ___/ /  __/ /__/ /_/ / /  / / /_/ /_/ /  / ___ |/ ____// /   
/____/\___/\___/\__,_/_/  /_/\__/\__, /  /_/  |_/_/   /___/   
                                /____/                        
""")

print("------------------------------------------")
print("Creating new Keys")
print("\n")
key = createKeys()
print("------------------------------------------")
print("\n")
startApi()