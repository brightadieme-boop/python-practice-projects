# Mini note App
filename = "my_notes.txt"

while True:
    print("\n--- Notes App ---")
    print("1. Add Note")
    print("2. view notes")
    print("3. Delete all notes")
    print("4. Exit")

    choice = input("Enter your choice(1-4): ")

    if choice == "1":
        note = input("Write your note: ")
        with open(filename, "a") as file: # 'a'  means append(add new note at the end)
            file.write(note + "\n")
            print("Note saved!")
        
    elif choice == "2":
        try:
            with open(filename, "r" ) as file:
                content = file.read()
                if content.strip() == "":
                   print("No notes found.")
                else:
                    print("\n--- Your Notes ---")
                    print(content)
        except FileNotFoundError:
            print("No notes file found yet. ")

    elif choice == "3":
        with open (filename, "w") as file:
            file.write("")
        print("All note deleted!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")        
