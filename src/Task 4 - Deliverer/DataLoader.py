from ApiHelper import ApiHelper
import random
import json
 
# Collects the Data the Helper needs
class DataLoader:
    def CollectData(Adress):
        # Product Suchen

        # return Data
        # Data must contain
        # SecurityCookie, Product

        SecurityCookie = ApiHelper.login(Adress)
        Product = DataLoader.getProduct()

        Body = {"SecurityCookie": SecurityCookie, "Product": Product}  

        return Body

    def getProduct():
        productsSheet = open("Product_Data")
        allJsons = productsSheet.readlines()

        selectedProduct = allJsons[random.randint(0, len(allJsons)-1)]

        Json = json.loads(selectedProduct)
        return Json['name']
        