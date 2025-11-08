print("Advanced Mini calculator - Day 2")

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter operation (+, -, *, /): ")

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                result = "Error: cannot divide by zero"
            else:
                result = num1 / num2
        else:
            result = "Error: Invalid operator"
        print("Result", result)
    except ValueError:
        print("Error: please enter valid numbers.") 

    # Ask if they want to continue
    again = input("Do you want calculate again? (yes/no): ").lower() 
    if again != "yes":
        print("Thanks for using the calculator. Goodbye!") 
        break                    