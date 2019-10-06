import requests
import os
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("USERS_API_ENPOINT")
class User:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.age = kwargs.get("age")

    def info(self):
        print(self.name, self.age)

    @staticmethod
    def fetch():
        response = requests.get(url)
        # data/ content
        print(response.status_code)
        # status code
        print(response.content)
