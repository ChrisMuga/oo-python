import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

# fetch .env variables
url = os.getenv("USERS_API_ENPOINT")


class User:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.age = kwargs.get("age")

    def info(self):
        print(self.name, self.age)

    @classmethod
    def fetch(cls):
        response = requests.get(url)
        # status code
        print(response.status_code)
        # data/content
        print(json.loads(response.content))

        list(map(lambda x: cls.parse_and_display(x.get("name")), json.loads(response.content)))

    @staticmethod
    def parse_and_display(item):
        # obtain item and print upper case result
        print(item.upper())
