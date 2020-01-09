from Database_Functions import Database_Functions
import Authentication_Service
import mysql.connector as mysql
import random

# ------------------------------------------
# API logic - Everything the API will do
class ApiLogic:
    adress = "SecurityService:5000"
    # Question with QuestionID
    def QuestionToTheServer( SecurityCookie, QuestionID, Database, query):
        
        body = """ { "Token" = %s } """

        finalbody = (body (SecurityCookie))


        # Role Of The User
        role = Authentication_Service.sendMessage(adress, finalbody)

        if role == "False":
            return "Error - User not allowed"


        # Nutzer beschränken
        if (role == "manager") and (QuestionID <= 5):
            return "Error - Not allowed"
        if (role == "customer") and (QuestionID >= 5):
            return "Error - Not allowed"

        # send query
        answer = sendQuery(query[QuestionID])

        # return result
        return answer


    # Question with own Script
    def SpecialQuestionToTheServer( SecurityCookie ,Query, Database):
        # Role of The User
        body = """ { "Token" = %s } """

        finalbody = (body (SecurityCookie))


        # Role Of The User
        role = Authentication_Service.sendMessage(adress, finalbody)

        if role == "False":
            return "Error - User not allowed"

        # Nutzer beschränken
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
    def Login( Password, UserName):
        body = """{"User" = %s,
            "Password" = %s}"""

        finalbody = (body, (UserName, Password))

        return Authentication_Service.sendMessage(adress, finalbody)
        

    # Bought
    def ProductBought( SecurityCookie, Data, Database):
        # check Role
        body = """ { "Token" = %s } """

        finalbody = (body (SecurityCookie))


        # Role Of The User
        role = Authentication_Service.sendMessage(adress, finalbody)

        if role != "helper":
            return "Error - User not allowed"


        # send query        
        Query = """INSERT INTO `Shop`.`Transactions` (`Products_ID`, `Type`, `ID`) VALUES (%s, %s, %s); """
        FinalQuery = (Query, (Data['Products_ID'], "bought",Data['ID']))
        sendQuery(FinalQuery, Database)

    # Delivered
    def ProductDelivered( SecurityCookie, Data, Database):
        # Role of The User
        body = """ { "Token" = %s } """

        finalbody = (body (SecurityCookie))


        # Role Of The User
        role = Authentication_Service.sendMessage(adress, finalbody)

        if role != "helper":
            return "Error - User not allowed"
        
        # send query
        Query = """INSERT INTO `Shop`.`Transactions` (`Products_ID`, `Type`, `ID`) VALUES (%s, %s, %s); """
        FinalQuery = (Query, (Data['Products_ID'], "delivered",Data['ID']))
        sendQuery(FinalQuery, Database)

    # Review made
    def Review( SecurityCookie, Product, Review, Database):
        body = """ { "Token" = %s } """

        finalbody = (body (SecurityCookie))

        # Role Of The User
        role = Authentication_Service.sendMessage(adress, finalbody)

        if role != "helper":
            return "Error - User not allowed"
        
        Customers_ID_Query = """ """
        Products_ID_Query = """ select ID from Shop.Products where Name = %s"""

        rating = random.randint(0,5)
        body = Review
        Customers_ID = "3"
        Products_ID = sendQuery((Products_ID_Query,(Product)), Database)

        # send query
        Query = """ INSERT INTO `Shop`.`Comments` (`Body`, `Rating`, `Customers_ID`, `Products_ID`) VALUES (%s, %s, %s, %s); """
        FinalQuery = (Query, (body, rating, Customers_ID, Products_ID))
        sendQuery(FinalQuery, Database)


    def queryloader():
        File = open("query.sql")
        query = File.readlines()
        return query

    def sendQuery( Query, Database):
        Cursor = Database.cursor()
        Cursor.execute(Query)
        return Cursor.fetchall()