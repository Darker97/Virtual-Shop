import security
import Database

# ------------------------------------------
# API logic - Everything the API will do

def StandartQuestionToTheServer(SecurityCookie, QuestionID, Database, query):
    if security.CanHeDoThat(SecurityCookie):
         return Database.SendQuery(query[QuestionID], Database)
    else:
        return "Error 413 - Data Forbidden"

def SpecialQuestionToTheServer(SecurityCookie, Data ,QuestionID, Database, query):
    if security.CanHeDoThat(SecurityCookie):
        if security.InjectionChecker(Data):
            Database.SendQuery(Data, Database)
        else:
            print("POSSIBLE INJECTION")
            print(Data)
    else:
        return "Error 413 - Data Forbidden"


def NewData(SecurityCookie, Data, DataID, Database, query):
    if security.CanHeDoThat(SecurityCookie):
        Query = (query[1], (Data))
        return Database.SendQuery(Query, Database)
    else:
        return "Error 413 - Data Forbidden"

def NewUser(SecurityCookie, Data, Database, query):
    if security.CanHeDoThat(SecurityCookie):
        Query = (query[2], (Data))
        return Database.SendQuery(Query, Database)
    else:
        return "Error 413 - No Admin"

def Login(Password, UserName, Database, query):
    # TODO
    return security.SecurityGiveUser(Password, UserName, Database)


def queryloader():
    File = open("query.sql")
    query = File.readlines()
    return query