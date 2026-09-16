# Transportation mode selection based on distance
# This program suggests a mode of transportation based on the distance to travel.

distance = float(input("Enter the distance to travel in kilometers: "))

if distance <= 3:
    print("You can walk.")
elif distance <= 15:
    print("You can bike.")
else:
    print("You can car.")