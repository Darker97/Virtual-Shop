import requests
import json

# Sends the given Data to the API
class ApiHelper:
    def Senddata(self, Adress, body):
        # SecurityCookie, Product, Review

        Adress += "/review"

        # put request
        sended = requests.put(Adress, params=body)
        return sended.json()

    def login(self):
        # load credentials
        file = open("credential.key")
        Data = json.load(file.readline())
        
        #UserName Password
        password = Data['Password']
        Username = Data['UserName']

        # sends login to API
        Adress = "/User"

        #UserName, Password
        body = """{ "UserName" = %s, "Password" = %s }"""

        return requests.put(Adress, params=(body,(Username, password)))