# Brandon Nelson
# 10/8/2024
# CSS 225 Module 3
# This program will compute the MPG for a car.
# Prompt the user to input the MPG.

import math

# MPG Calculator using math module
def calculate_mpg():
    try:
        # Prompts the user for input.
        miles_driven = float(input("Enter the number of miles driven: "))
        gallons_used = float(input("Enter the number of gallons used: "))

        # Calculate the MPG.
        mpg = miles_driven / gallons_used

        # This uses math to round the result to two decimal places.
        mpg_rounded = math.floor(mpg * 100) / 100

        # The results and final MPG.
        print(f"\nYour car's fuel efficiency is: {mpg_rounded:.2f} miles per gallon.")

    except ValueError:
        print("Please enter valid numerical values.")

calculate_mpg()
