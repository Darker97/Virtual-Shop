import requests
import json

# Sends the given Data to the API
class ApiHelper:
    def Senddata( Adress, body):
        # SecurityCookie, Product, Review

        Adress += "/Product"

        # put request
        sended = requests.get(Adress, data=body)
        return sended.json()

    def login(Adress):
        # load credentials
        file = open("credential.key")
        line = file.readline()
        Data = json.loads(line)
        
        #UserName Password
        password = Data['Password']
        Username = Data['UserName']

        # sends login to API
        Adress += "/User"

        #UserName, Password
        params = {"Password": password, "UserName": Username}

        return requests.get(Adress, data= params)