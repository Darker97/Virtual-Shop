import security

# ------------------------------------------
# API logic - Everything the API will do

def QuestionToTheServer(SecurityCookie, QuestionID):
    if security.CanHeDoThat():
        return
    else:
        return "Error 413 - Data Forbidden"

def NewData(SecurityCookie, Data, DataID):
    if security.CanHeDoThat():
        return
    else:
        return "Error 413 - Data Forbidden"

def NewUser(SecurityCookie, Data):
    if security.CanHeDoThat():
        return
    else:
        return "Error 413 - No Admin"

def Login(Password, UserName):
    try:
        return security.SecurityGiveUser()
    except:
        return "Error 413 - Not a User"