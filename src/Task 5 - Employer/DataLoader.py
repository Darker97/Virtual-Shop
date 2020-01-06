import ApiHelper
import random
import json

# Collects the Data the Helper needs
class DataLoader:
    def CollectData(self):
        # Product Suchen

        # return Data
        # Data must contain
        # SecurityCookie, Product

        SecurityCookie = ApiHelper.login()
        Product = getProduct()

        Body = """{"SecurityCookie" = %s, "Product" = %s}  """

        return (Body, (SecurityCookie, Product))

    def getProduct(self) -> String:
        productsSheet = open("Product_DATA")
        allJsons = productsSheet.readlines()

        selectedProduct = allJsons[random.randint(0, allJsons.count()-1)]

        Json = json.load(selectedProduct)
        return Json['name']
        