# BMI Calculator with Error Handling
def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"
while True:    
    try:
        weight = float(input("Enter your weight in kg. "))
        height = float(input("Enter your height in meters: "))
        bmi = calculate_bmi(weight, height)
        status = interpret_bmi(bmi)
        print(f"Your BMI is {bmi}. You are {status}.")
    except ValueError:
        print("please enter valid number for weight and height")

    again = input("Do you want to calculate again? (yes/no?): ").lower()
    if again != "yes":
        print("Goodbye!")
        break       