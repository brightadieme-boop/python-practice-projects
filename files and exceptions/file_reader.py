from pathlib import Path
path = Path('files and exceptions/pi_digits.txt')
contents = path.read_text()
contents = contents.rstrip()
lines = contents.splitlines()
for line in lines:
    print(line)