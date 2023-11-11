#Enter the width of the tire in mm (ex 205): 185
#Enter the aspect ratio of the tire (ex 60): 50
#Enter the diameter of the wheel in inches (ex 15): 14

#The approximate volume is 24.09 liters


import math

w = float(input("Width of the tire in mm (ex 205): "))
a = float(input("Aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

total = (((math.pi * (w**2) * a)) * ((w * a) + (2540 * d)) / 10000000000)

print(f"Volume: {total: .2f}L")