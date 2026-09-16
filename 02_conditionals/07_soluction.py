# Password Strength Checker
# This program checks the strength of a password based on its length.

password = input("Enter your password: ")
length = len(password)

if length < 6:
    print("Weak password")
elif length < 10:
    print("Moderate password")
else:
    print("Strong password")