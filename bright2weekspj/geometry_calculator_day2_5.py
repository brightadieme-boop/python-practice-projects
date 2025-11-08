import math

print("Welcome to the Geometry Calculator!")
while True:
    print("\nChoose what you want to calculate:")
    print("1. Area of a Circle")
    print("2. Area of a Rectangle")
    print("3. Area of a Triangle")

    choice = input("Enter 1, 2 or 3: ")

    if choice == "1":
        try:
            radius = float(input("Enter the radius of the circle:"))
            if radius < 0:
              print("Error: Radius cannot be negative.")
            else:
                area = 3.14159 * radius * radius
                print("Area of circle is:", round(area, 2))   
        except ValueError:
           print("Error: please enter a valid number for the radius")

    elif choice == "2":
        try:
            length = float(input("Enter the lenght of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))

            if length < 0 or width < 0:
                print("Error: Length and width must be positive numbers.")
            else:
                 area = length * width
                 print("Area of the rectangle is:", round(area, 2))
        except ValueError:
            print("Error: please enter valid number for length and width.")         

    elif choice == "3":
        try:
            base = float(input("Enter the base of the triangle:"))
            height = float(input("Enter the height of the triangle:"))

            if base < 0 or height < 0:
                print("Error: Base and height must be positive numbers.")
            else:    
                 area = 0.5 * base * height
                 print("Area of the traiangle is:", round(area, 2))
        except ValueError: 
            print("Error: Please enter valid numbers for base and height.")         

    else:
        print("invalid choice. Please enter 1, 2 or 3.")

    again = input("\nDo you want to calculate again? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye!")
        break               