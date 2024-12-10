import math

# area = pi * r²

radius = float(input("Enter the radius of circle: "))
area = math.pi * pow(radius, 2)
print(f"The area of the circle is: {round(area,2)} cm²")
