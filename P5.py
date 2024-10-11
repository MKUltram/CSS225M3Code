# Brandon Nelson
# 10/8/2024
# CSS 225 Module 3
# The program will convert degrees Fahrenheit to degrees Celsius.

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0


def temperature_conversion():
    try:
        # Ask the user to input the temperature in Fahrenheit.
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

        # Convert the temperature to Celsius.
        celsius = fahrenheit_to_celsius(fahrenheit)

        # Check the temperature range and print the appropriate message.
        if fahrenheit < 30:
            print(f"That's cold! In Norway, you would say it is {celsius:.2f} degrees Celsius.")
        elif 30 <= fahrenheit <= 70:
            print(f"That's balmy! In Japan, you would say it is {celsius:.2f} degrees Celsius.")
        else:
            print(f"That's hot! In Brazil, you would say it is {celsius:.2f} degrees Celsius.")

    except ValueError:
        print("Please enter a valid number for the temperature.")

# Run the program.
temperature_conversion()
