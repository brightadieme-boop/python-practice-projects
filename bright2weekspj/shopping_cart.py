cart = []

print("Welcome to Bright's Shopping Cart Calculator!")
print("Enter the price of each item.")
print("Type 'done' when you're finished.\n")

while True:
    price = input("Enter item price: ")
    if price.lower() == "done":
        break
    try:
        price = float(price)
        cart.append(price)
    except ValueError:
        print("Please enter a valid number.")
total = sum(cart)
count = len(cart)

print(f"\n You added {count} items.Total cost is: £{round(total, 2)} ")