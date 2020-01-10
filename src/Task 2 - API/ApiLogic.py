from Database_Functions import Database_Functions
from Authentication_Service import Authentication_service
import mysql.connector as mysql
import random

# ------------------------------------------
# API logic - Everything the API will do
class ApiLogic:
    adress = "SecurityService:5000"
    # Question with QuestionID
    def QuestionToTheServer( SecurityCookie, QuestionID, Database, query):
        
        # body = """ { "Token" = %s } """

        # finalbody = (body (SecurityCookie))


        # Role Of The User
        # role = Authentication_Service.sendMessage(adress, finalbody)
        role = "Test"

        if role == "False":
            return "Error - User not allowed"


        # Nutzer beschränken
        if (role == "manager") and (QuestionID <= 5):
            return "Error - Not allowed"
        if (role == "customer") and (QuestionID >= 5):
            return "Error - Not allowed"


        answer = ""
        # send query
        temp = int(QuestionID)
        finalQuery = query[temp]
        try:
            answer = ApiLogic.sendQuery(finalQuery, Database)
        except Exception as e:
            answer = "SQL ERROR " + str(e)

        try:
            Database.cursor().fetchall()
        except Exception as e:
            answer = str(e)
        
        # return result
        return answer, 200


    # Question with own Script
    def SpecialQuestionToTheServer( SecurityCookie ,Query, Database):
        # Role of The User
        # body = """ { "Token" = %s } """

        # finalbody = (body (SecurityCookie))


        # Role Of The User
        # role = Authentication_Service.sendMessage(adress, finalbody)

        role = "admin"

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
        answer = ApiLogic.sendQuery(Query)
        try:
            Database.cursor().fetchall()
        except Exception as e:
            answer = str(e)

        # return result
        return answer, 200


    # Login
    def Login( Password, UserName):
        adress = "/security/login"
        body = {"User": UserName, "Password": Password}
        return Authentication_Service.sendMessage(adress, body)
        

    # Bought
    def ProductBought( SecurityCookie, Data, Database):
        # check Role
        # body = """ { "Token" = %s } """

        # finalbody = (body (SecurityCookie))


        # Role Of The User
        # role = Authentication_Service.sendMessage(adress, finalbody)
        role = "helper"
        
        if role != "helper":
            return "Error - User not allowed"

        Product = Data
        ID = 0

        # send query        
        Query = """INSERT INTO `Shop`.`Transactions` (`Type`, `Products_Name`) VALUES (%s, %s);"""
        FinalQuery =  "bought", Product

        try:
            Database.cursor(buffered=True).execute(Query ,FinalQuery)
            Database.commit()
            Database.cursor().close()
        except Exception as e:
            return(str(e))
        

        return "Success"


    # Delivered
    def Productdeliverd( SecurityCookie, Data, Database):
        # Role of The User
        # body = """ { "Token" = %s } """

        # finalbody = (body (SecurityCookie))


        # Role Of The User
        # role = Authentication_Service.sendMessage(adress, finalbody)

        role = "helper"

        if role != "helper":
            return "Error - User not allowed"
        
        Product = Data
        ID = 0

        # send query
        Query = """INSERT INTO `Shop`.`Transactions` (`Type`, `Products_Name`) VALUES (%s, %s);"""

        FinalQuery = "delivered", Product

        try:
            Database.cursor(buffered=True).execute(Query ,FinalQuery)
            Database.commit()
            Database.cursor().close()
        except Exception as e:
            return(str(e))

        return "Success"

    # Review made
    def Review( SecurityCookie, Product, Review, Database):
        # body = """ { "Token" = %s } """

        # finalbody = (body (SecurityCookie))

        # Role Of The User
        # role = Authentication_Service.sendMessage(adress, finalbody)

        role = "helper"

        if role != "helper":
            return "Error - User not allowed"
        
        Customers_ID_Query = """ """
        Products_ID_Query = """ select ID from Shop.Products where Name = %s"""

        rating = random.randint(0,5)
        body = Review
        Customers_ID = random.randint(0,200)

        # send query
        Query = """ INSERT INTO Shop.Comments (Body, Rating, Customers_ID, Products_Name) VALUES (%s, %s, %s, %s); """
        FinalQuery = body, rating, Customers_ID, Product
        try:
            Database.cursor(buffered=True).execute(Query ,FinalQuery)
            Database.commit()
            Database.cursor().close()
        except Exception as e:
            return(str(e))

        return "Success"


    def queryloader():
        File = open("query.sql")
        query = File.readlines()
        return query

    def sendQuery( Query, Database):
        Cursor = Database.cursor()
        try:
            Cursor.execute(Query)
        except Exception as e:
            return str(e)
        
        Database.commit()
        Data = Cursor.fetchall()
        array = []
        for each in Data:
            array.append(str(each))
        Cursor.close()
        return str(array)