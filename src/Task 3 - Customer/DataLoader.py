from ApiHelper import ApiHelper
import random
import json

# Collects the Data the Helper needs
class DataLoader:
    def CollectData(Adress):
        # Product Suchen


        # nächster Kommentar

        # return Data
        # Data must contain
        # SecurityCookie, Product, Review

        SecurityCookie = ApiHelper.login(Adress)
        Product = DataLoader.getProduct()
        Review = DataLoader.getReview()

        Body = {"SecurityCookie": SecurityCookie, "Product": Product, "Review": Review}

        return Body

    def getProduct():
        productsSheet = open("Products")
        allJsons = productsSheet.readlines()

        selectedProduct = allJsons[random.randint(0, len(allJsons)-1)]

        Json = json.loads(selectedProduct)
        return Json['name']
        


    def getReview():
        AllComments = open("comments.csv").readlines()
        temp = AllComments.pop(random.randint(0, len(AllComments)))
        return temp
        