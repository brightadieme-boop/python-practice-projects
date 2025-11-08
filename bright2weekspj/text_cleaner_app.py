text = input("Enter a sentence: ")

while True:
    print("\nWhat would you like to do?")
    print("1. UPPERCASE")
    print("2. lowercase")
    print("3. Title Case")
    print("4. Remove Extra Spaces")
    print("5. Replace 'a' with '@'")
    print("6. Count Words")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        print(text.upper())
    elif choice == "2":
        print(text.lower())
    elif choice == "3":
        print(text.title())
    elif choice == "4":
        print(" ".join(text.split()))
    elif choice == "5":
        print(text.replace('a','@'))
    elif choice == "6":
        print(len(text.split()))
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
