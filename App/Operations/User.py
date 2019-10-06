import requests
import os
url = os.getenv("USERS_API_ENPOINT")
class User:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.age = kwargs.get("age")

    def info(self):
        print(self.name, self.age)

    @staticmethod
    def fetch():
        requests.get(url)
