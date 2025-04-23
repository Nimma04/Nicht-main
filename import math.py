import math

def calculate_2d_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# گرفتن مختصات از کاربر
x1 = float(input("X erste Punkt"))
y1 = float(input("Y erste Punkt"))
x2 = float(input("X Zweite Punkt"))
y2 = float(input("Y Zweite Punkt"))

distance = calculate_2d_distance(x1, y1, x2, y2)

print(f"Distance Zwischen 2 Punkte: {distance}")
