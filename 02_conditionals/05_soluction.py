# Weather Activity Suggestion
# This program suggests an activity based on the weather condition.

weather = input("Enter the weather condition (sunny, rainy, snowy): ").strip().lower()  

if weather == "sunny":
    print("It's a great day for a walk in the park!")
elif weather == "rainy":
    print("Perfect weather to read a book indoors.")
elif weather == "snowy":
    print("How about building a snowman?")
else:
    print("I'm not sure what activity to suggest for this weather.")