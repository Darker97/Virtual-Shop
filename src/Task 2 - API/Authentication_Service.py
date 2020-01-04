import requests

class Authentication_service:
    def sendMessage(self, Adress, body):
        file = open("./Authentication.setup")
        FinalAdress = (file.readlines[0] + Adress)
        request = requests.get(FinalAdress, params=body)
        return request.json()
