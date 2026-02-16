print("==================\nArea Calculator 📐\n==================\n\n1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit")

shape = int(input("\nEnter the number of the shape you want to calculate the area of: "))

if shape == 1:
    base = float(input("\nEnter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area_triangle = 0.5 * base * height
    print(f"The area of the triangle is: {area_triangle}")

if shape == 2:
    length = float(input("\nEnter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area_rectangle = length * width
    print(f"The area of the rectangle is: {area_rectangle}")

if shape == 3:
    side = float(input("\nEnter the side length of the square: "))
    area_square = side * side
    print(f"The area of the square is: {area_square}")

if shape == 4:
    radius = float(input("\nEnter the radius of the circle: "))
    area_circle = 3.14 * radius * radius
    print(f"The area of the circle is: {area_circle}")

if shape == 5:
    print("\nGoodbye!")