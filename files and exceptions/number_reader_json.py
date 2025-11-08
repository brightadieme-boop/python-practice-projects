from pathlib import Path
import json
#Reading files
path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)