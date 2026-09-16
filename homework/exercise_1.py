# Print all the odd numbers between 1 and 20
for i in range(1, 21):
    if i % 2 != 0:
        print(i)

# Print the multiplication table of 57
for i in range(1, 11):
    print(i*57)

# Print all the numbers between 3 and 50 that are divisible by 3 and skip the number 15.
for i in range(3, 51, 3):
    if i== 15:
        continue
    print(i)


# Take two numbers as input from the user and print all the numbers between 1 and 1000 that are divisible by both of those numbers.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

for i in range(1, 1001):
    if i % num1 == 0 and i % num2 == 0:
        print(i)