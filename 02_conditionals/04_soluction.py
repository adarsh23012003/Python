# Fruit Ripeness Checker
# This program checks the ripeness of a fruit based on its color.

fruit_color = input("Enter the color of the fruit (green, yellow, brown): ").strip().lower()

if fruit_color == "green":
    print("The fruit is unripe.")
elif fruit_color == "yellow":
    print("The fruit is ripe.")
elif fruit_color == "brown":
    print("The fruit is overripe.")
else:
    print("Unknown fruit color.")