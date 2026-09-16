# Grade Calculator

grade = float(input("Enter your grade (0-100): "))

if grade < 0 or grade >= 100:
    print("Invalid grade.")
    exit()

if grade >= 90:
    print("You received an A.")
elif grade >= 80:
    print("You received a B.")
elif grade >= 70:
    print("You received a C.")
elif grade >= 60:
    print("You received a D.")
else:
    print("You received an F.")