"""
Write a Python program that asks the user for three numbers:

A starting odometer value in miles
An ending odometer value in miles
An amount of fuel in gallons
Your program must calculate and print fuel efficiency in both miles per gallon and liters per 100 kilometers. 

Your program must have three functions named as follows:
main
miles_per_gallon
lp100k_from_mpg

All user input and printing must be in the main function. 
In other words, the miles_per_gallon and lp100k_from_mpg functions must not call the input or print functions.
"""

def main():
    
    start_odometer = float(input("enter the start odometer"))
    end_odometer = float(input("enter the end odometer"))
    gallons = float(input("Enter the number of gallons"))
    miles_efficiency = miles_per_gallon(start_odometer, end_odometer, gallons)
    km_efficiency = lp100k_from_mpg(miles_efficiency)
    

    print(f"{miles_efficiency:.2f}")
    print(f"{km_efficiency:.2f}")
    


def miles_per_gallon(start, end, gallons):

    mpg = (end - start) / gallons

    return mpg


def lp100k_from_mpg(mpg):

    lp100k = 235.215/mpg

    return lp100k


main()