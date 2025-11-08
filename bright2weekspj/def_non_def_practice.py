while True:
    print("Welcome to No-Function Calculator")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

    choice = input("Choose an operation (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        if choice == '1':
            result = num1 + num2
        elif choice == '2':
            result = num1 - num2
        elif choice == '3':
            result = num1 * num2
        elif choice == '4':
            if num2 == 0:
                 result = "Error: Division by zero"
            else:
                result = num1 / num2
        print("Result", result)
    else:
        print("Invalid choice.")
    again = input("Calculate again? (yes/no): ")
    if again.lower() != 'yes':
        break                      
            