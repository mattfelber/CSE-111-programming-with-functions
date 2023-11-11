import math
from datetime import datetime

w = float(input("Width of the tire in mm (ex 205): "))
a = float(input("Aspect ratio of the tire (ex 60): "))
d = float(input("Diameter of the wheel in inches (ex 15): "))

total = (((math.pi * (w**2) * a)) * ((w * a) + (2540 * d)) / 10000000000)

print(f"Volume: {total: .2f}L")

total = round(total, 2)
today = datetime.now()
today = f"{today: %Y-%m-%d}"

with open('volumes.txt', "a") as volume_file:
    volume_file.write(f"\nCurrent date: {str(today)}"
                      f"\nWidth = {str(w)}"
                      f"\nAspect ratio = {str(a)}"
                      f"\nDiameter = {str(d)}"
                      f"\nVolume = {str(total)}")