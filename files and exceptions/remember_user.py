from pathlib import Path
import json

path = Path('username.json')
if path.exists():
 contents = path.read_text()
 username = json.loads(contents)
 print(f"Welcome back, {username}!")

else:
 username =  input("Please enter name ")
 contents = json.dumps(username)
 path.write_text(contents)
 print(f"I will remember you when you come back, {username}!")
