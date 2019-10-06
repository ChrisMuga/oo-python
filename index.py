from dotenv import load_dotenv
import os
from App import Operations

load_dotenv()
app_name = os.getenv("APP_NAME")

print(app_name)
Operations.info(name="Tom Mboya")
