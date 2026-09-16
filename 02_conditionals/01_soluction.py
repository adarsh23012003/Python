# Age Group Categorization

age = input("Provide me your age: ")
age = int(age)

if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are an adult.")
elif age < 60:
    print("You are a senior.")
else:
    print("You are an elder.")