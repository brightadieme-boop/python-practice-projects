while True:
    print("Area of a Square calculator")
    try:
        side = float(input("Enter lenght of one side:"))
        if side < 0:
            print("side cannot be nagative. Try again.")
            continue
        area = side * side
        print("Area of the square is:", round(area, 2))
    except ValueError:
        print("Error: Please enter a valid number.")

    again = input("Do you want to calculate again? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye!")
        break         