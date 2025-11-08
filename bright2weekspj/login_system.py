
import getpass

users = []

while True:
    print("\n---Welcome Bright Login System ----")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        username = input("Enter a username: ")
        password = getpass.getpass("Enter a password: ")
        users.append({"username": username, "password": password})
        print("Registration successful!")

    elif choice == "2":
        username = input("Enter your username: ")
        password = input("Enter your password ")

        username_exists = False
        for user in users:
            if user["username"] == username and user["password"] == password:
                print("Login successful welcome,", username)
                found = True
            if user["username"] == username:
                username_exists = True    
                break
            if not found:
                print("Login failed. Incorrect username or password.")
            if username_exists:
                print("usename already taken. Try a diffrent one.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again")                