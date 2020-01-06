import ApiHelper
import random
import json

# Collects the Data the Helper needs
class DataLoader:
    def CollectData(self):
        # Product Suchen


        # nächster Kommentar

        # return Data
        # Data must contain
        # SecurityCookie, Product, Review

        SecurityCookie = ApiHelper.login()
        Product = getProduct()
        Review = getReview()

        Body = """{"SecurityCookie" = %s, "Product" = %s, "Review" = %s}  """

        return (Body, (SecurityCookie, Product, Review))

    def getProduct(self) -> String:
        productsSheet = open("Product_DATA")
        allJsons = productsSheet.readlines()

        selectedProduct = allJsons[random.randint(0, allJsons.count()-1)]

        Json = json.load(selectedProduct)
        return Json['name']
        


    def getReview(self) -> String:
        AllComments = open("comments.csv").readlines()
        return AllComments[random.randint(0, AllComments.count)]
        