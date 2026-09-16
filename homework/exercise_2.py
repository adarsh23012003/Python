# Given a list of roll numbers: ["101", "102", "104", "104", "105", "106", "105", "108", "109", "110"]. Print all unique roll numbers in the list.

roll_numbers = ["101", "102", "104", "104", "105", "106", "105", "108", "109", "110"]
unique_roll_numbers = set(roll_numbers)
for roll in unique_roll_numbers:
    print(roll)


data =[(101,"Adarsh",56000), (102,"Amit",45000), (103,"Rohit",60000), (104,"Suresh",70000), (105,"Ramesh",50000)]

input_roll = int(input("Enter the roll number: "))

for roll, name, salary in data:
    if roll == input_roll:
        print(f"Name: {name}")
        print(f"Salary: {salary}")
        break