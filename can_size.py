"""
The storage efficiency of a steel can is computed by dividing the volume of a can by its surface area.
Work as a team to write a Python program named can_sizes.py that computes and prints the storage efficiency for each of the following 12 steel can sizes.
Then visually examine the output and answer this question, “Which can size has the highest storage efficiency?”
"""

import math


can = "picnic"
radius = 6.83
height = 10.16



def main():
    vol = compute_volume(radius, height)
    surface = compute_surface_area(radius, height)
    #print(f"Volume: {vol:.2f}")
    #print(f"Surface: {surface:.2f}")
    efficiency = vol / surface
    print(f"Efficiency: {efficiency:.2f}")



def compute_volume(radius, height):
    volume = math.pi * radius ** 2 * height

    return volume



def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)

    return surface_area


main()