to_do_list = []

while True:
    print("\nWhat would you like to do?")
    print("1. Add task. ")
    print("2. Mark as done. ")
    print("3. Remove a task. ")
    print("4. View task")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        task = input("Enter a task: ")
        to_do_list.append({"task": task, "done": False})
        print("Task added")

    elif choice == "2":
        for i,t in enumerate(to_do_list):
            status = "checked" if t["done"] else "unchecked"
            print(f"{i+1}. {t['task']} [{status}]")
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(to_do_list):
            to_do_list[index]["done"] = True
            print("Marked as done!")
        else:
            print("Invalid task number.")

    elif choice == "3":
        for i, t in enumerate(to_do_list):
            print(f"{i+1}. {t['task']}")
        index = int(input("Enter task number to remove: ")) - 1 
        if 0 <= index < len(to_do_list):
            removed = to_do_list.pop(index)
            print(f"Removed task: {removed['task']}")
        else:
            print("Invalid task number.")

    elif choice == "4":
        print("\nYour Tasks:")
        for i, t in enumerate(to_do_list):
            status = "checked" if t["done"] else "unchecked"
            print(f"{i+1}. {t['task']} [{status}]")

    elif choice == "5":
        print("Goodbye!")
        break
    else:
      print("Invalid option. Try again. ")                                     
         