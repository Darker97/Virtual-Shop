import requests

# Sends the given Data to the API
class ApiHelper:
    def Senddata(self, Adress, body):

        # put request
        sended = requests.put(Adress, params=body)
        return sended.json()