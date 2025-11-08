print("=" * 40)
print("    Parallelogram Area Calculator")
print("=" * 40)

while True:
    print("Area if parallelogram calculator")

    try:
        base = float(input("Enter the base of the parallelogram:"))
        height = float(input("Enter the height of the parallelogram:"))
        area = base * height
        print("Area of the parallelogram is:",round(area, 2))

    except ValueError:
        print("Error: please enter valid numbers for base and height.")

    again = input("Do you want to calculate again? (yes/no)").lower()
    if again != "yes":
        print("Goodbye!")
        break 
            