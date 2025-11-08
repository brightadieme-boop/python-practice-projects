print("\nBasic Calculator No Error handling. ")

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
agaian = input("do you want to calculate again? (yes/no)")
if agaian != "no":
    print("Thank you Goodbye!")
    
    


