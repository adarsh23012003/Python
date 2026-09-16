# Movie Ticket Pricing

age = input("Provide me your age: ")
day = "Wednesday"
age = int(age)

price = 12 if age >= 18 else 8

if day == "Wednesday":
    # price = price-2
    price -= 2

print("Ticket price is:", price)