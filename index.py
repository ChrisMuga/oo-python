from dotenv import load_dotenv
import os
from App import Operations
from App.Operations.User import User

load_dotenv()
app_name = os.getenv("APP_NAME")
Operations.info(name="Tom Mboya")

user = User(name="Chris Muga", age=25)
users = user.fetch()
user.print_names(users)
