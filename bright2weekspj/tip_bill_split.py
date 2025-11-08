print("Welcome to the tip & Bill split calculator!\n")
bill = float(input("Enter the total bill amount: £"))
tip_percent = float(input("Enter the percentage(e.g., 10, 15, 20): "))
people = int(input("How many people are splitting the bill? "))

tip_amount = bill * (tip_percent / 100)
total_bill= bill + tip_amount
share_per_person = total_bill / people

print("\n------Summary------")
print(f"Original Bill: £{bill}")
print(f"Tip ({tip_percent}%): £{round(tip_amount, 2)} ")
print(f"Total Bill With Tip: £{round(total_bill, 2)}")
print(f"Each person should pay: £{round(share_per_person, 2)}")