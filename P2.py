# Brandon Nelson
# 10/8/2024
# CSS 225 Module 3
# The program Prompts user for their name.

print("What is your name?")
name = input("Enter your Name:")

# The authorized users.
name1 = "Brandon"
name2 = "Benjamin"

# Check if the user is authorized.
if name == name1:
    print(f"Hello, {name1}!")
elif name == name2:
    print(f"Hello, {name2}!")
else:
    print("Unauthorized User")

