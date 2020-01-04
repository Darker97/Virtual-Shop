import security
import Database
import Authentication_Service
import mysql.connector as mysql

# ------------------------------------------
# API logic - Everything the API will do
class ApiLogic:

    # Question with QuestionID
    def QuestionToTheServer(self, SecurityCookie, QuestionID, Database, query):
        adress = ""
        body = """ { "Token" = %s } """

        finalbody = (body (SecurityCookie))


        # Role Of The User
        role = Authentication_Service.sendMessage(adress, finalbody)

        if role == "False":
            return "Error - User not allowed"


        #TODO Nutzer beschränken
        if (role == "manager") and (QuestionID <= 5):
            return "Error - Not allowed"
        if (role == "customer") and (QuestionID >= 5):
            return "Error - Not allowed"

        # send query
        answer = sendQuery(query[QuestionID])

        # return result
        return answer

        pass


    # Question with own Script
    def SpecialQuestionToTheServer(self, SecurityCookie ,Query, Database):
        # Role of The User
        adress = ""
        body = """ { "Token" = %s } """

        finalbody = (body (SecurityCookie))


        # Role Of The User
        role = Authentication_Service.sendMessage(adress, finalbody)

        if role == "False":
            return "Error - User not allowed"

        #TODO Nutzer beschränken
        if role != "admin":
            return "Error - User not an Admin"

        # check Query
        adress = ""
        body = """ {"question" = %s} """

        if Authentication_Service.sendMessage(adress, body) == "False":
            return "ERROR - Injection!"

        # send query
        answer = sendQuery(Query)

        # return result
        return answer


    # Login
    def Login(self, Password, UserName):
        adress = ""
        body = """{"User" = %s,
            "Password" = %s}"""

        finalbody = (body, (UserName, Password))

        return Authentication_Service.sendMessage(adress, finalbody)
        

    # Bought
    def ProductBought(self, SecurityCookie, Data):
        # check Role

        # send query

        pass

    # Delivered
    def ProductDelivered(self, SecurityCookie, Data):
        # check Role
        
        # send query

        pass


    def queryloader():
        File = open("query.sql")
        query = File.readlines()
        return query

    def sendQuery(Query, Database):
        Cursor = Database.cursor()
        Cursor.execute(Query)
        return Cursor.fetchall()