from pathlib import Path
path = Path('files and exceptions/24 H.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"sorry, the file {path} does not exist.")
else:
    #count the approximate number of the word in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The {path} has {num_words} words")
