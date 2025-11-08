grocery_list = []

while True:
    print("\nWhat would you like to do?")
    print("1. Add item")
    print("2. View list")
    print("3. Remove item")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
       while True: 
        item = input("Enter item to Add: ")
        grocery_list.append(item)
        print(f"'{item}' added to the list.")
        again = input("Do you want to add more items? (yes/no): ")
        if again != "yes":
            break

    elif choice == "2":
        if grocery_list:
            print("\n Grocery List")
            for b, item in enumerate(grocery_list, 1):
                print(f"{b}.{item}")
        else:
            print("Your list is empty.")

    elif choice == "3":
        if grocery_list:
            print("\nGrocery List")
            for b, item in enumerate(grocery_list, 1):
                print(f"{b}, {item}")

            try:
                remove_index = int(input("Enter the number of the item to remove: "))
                if 1 <= remove_index <= len(grocery_list):
                    removed_item = grocery_list.pop(remove_index - 1)
                    print(f"{removed_item} has been removed from the list.")
                else:
                    print("Invalid item number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Your list is empty.")                    

    elif choice == "4":
        print("Goodbye! Your final list:")
        print(grocery_list)
        break

    else:
        print("Invalid choice. Please select 1, 2, 3 or 4.")  