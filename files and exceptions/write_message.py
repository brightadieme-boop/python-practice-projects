#how to write one or multiple lines to a file
from pathlib import Path

contents = 'I love programming language.\n'
contents += 'I love solving problems in a simple but efficient way.\n'
contents += 'I love python language.\n'
contents += 'GOD is Awsome GOD! :).\n '

path = Path('files and exceptions/programming.txt')
path.write_text(contents)


