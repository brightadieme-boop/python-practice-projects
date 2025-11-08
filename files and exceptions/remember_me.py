#Saving user-generated data
from pathlib import Path
import json

username = input("Enter username ")

path = Path("username.json")
contents = json.dumps(username)
path.write_text(contents)

print(f"I will remember you when you come back {username}")