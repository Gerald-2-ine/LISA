#Area of a Triangle 1/2 base * height
Base = int(input("Enter your Base value: " ))
Height = int(input("Enter your Height value: "))

Area = (1/2* Base) * Height
print('Area of a Triangle:', float(Area),'cm^2')

#Area of a Trapezium = (a + b /2) * h

a = int(input("Enter your base a value: "))
b = int(input("Enter your base b value: "))
Height = int(input("Enter your Height value: "))
Area = (a + b / 2) * Height
print('Area of a Trapezium:', int(Area),'m^2')

#Converting Radians to Celsius

import math
def radians_to_degrees(radians):
    degrees = radians * (180 / math.pi)
    return degrees
radians = float(input("Enter an angle in radians: "))
degrees = radians_to_degrees(radians)
print(f"{radians} radians is equal to {degrees}°")