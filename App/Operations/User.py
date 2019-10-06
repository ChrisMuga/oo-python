import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

# fetch .env variables
url = os.getenv("USERS_API_ENDPOINT")


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
        print("status code:", response.status_code)
        # data/content
        data = json.loads(response.content)
        # print(json.loads(response.content))

        # print items from list
        cls.print_names(data)

    @staticmethod
    def parse_and_display(item):
        # obtain item and print upper case result
        print(item.upper())

    @classmethod
    def print_names(cls, data):
        list(map(lambda x: cls.parse_and_display(x.get("name")), data))
