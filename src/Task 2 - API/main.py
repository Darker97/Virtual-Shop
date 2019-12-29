from flask import Flask
from flask_restful import Api, Resources, reparse

# ------------------------------------------
main()

# ------------------------------------------


def main():
    pass


class Data(Resources):
    def get(self, info):
        return info + "" + "--> Jay, Works :D"
        pass

    def post(self, Function, Data):
        pass

    def put(self):
        pass
