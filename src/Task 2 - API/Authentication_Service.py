import requests

class Authentication_service:
    def sendMessage( Adress, body):
        file = open("./Authentication.setup")
        FinalAdress = (file.readlines[0] + Adress)
        sended = requests.get(FinalAdress, data=body)
        return sended
