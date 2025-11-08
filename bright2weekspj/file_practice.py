#Writing to a file
with open("notes.txt", "w") as file:
    file.write("Hello Bright!\n")
    file.write("This is your first file in Python.\n")

    # Reading from the file
    with open("notes.txt", "r") as file:
        content = file.read()
        print("File content:")
        print(content)