#Reading user-generated data
from pathlib import Path
import json

path = Path('username.json')
contents = path.read_text()
useername = json.loads(contents)

print(f"Welcome back {useername}")
