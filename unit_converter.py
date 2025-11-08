print("Welcome to the Unit Converter!")
print("Choose Operation")
print("1. Kilometers to Miles")
print("2. Centimeters to Inches")
print("3. Kilograms to pounds")

choice = input("Enter your choice (1/2/2):")

while True:
    try:
      if choice == "1":
        km = float(input("Enter distance in kilometers: "))
        miles = km * 0.621371
        print(f"{km} kilometer = {round(miles, 2)}miles")

      elif choice == "2":
        cm = float(input("Enter length in centimeters: "))
        inches = cm * 0.393701
        print(f" {cm} cm = {round(inches, 2)} inches")

      elif choice == "3":
        kg = float(input("Enter weight in kilograms: "))
        pounds = kg * 2.20462
        print(f" {kg} kilogram = {round(pounds, 2)} pounds")

      else:
        print("Invalid choice. Please enter 1, 2, or 3. ")
    except ValueError:
      print("Error: please enter valid inputs")

      again = input("Do you want to calculate again? (yes/no)").lower()
      if again != "yes":
        print("thanks for using the calculator, Goodbye!")
        break 



