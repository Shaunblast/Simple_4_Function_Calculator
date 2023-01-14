# Make the functions for the calculator
def addition(x, y):
    return print(x + y)

def subtraction(x, y):
    return print(x - y)

def multiplication(x, y):
    return print(x * y)

def division(x, y):
    return print(x / y)

# Save the inputs from the user into variables
calculation_decision = input("Insert addition, subtraction, multiplication, or division: ")
x = input("Please input a number: ")
y = input("Please input a second number: ")

# Nestle my if statements for which operation to call in a try and except statement to make sure that the
# user input the correct operation and two numbers
try:
    if calculation_decision == "addition":
        addition(float(x), float(y))
    elif calculation_decision == "subtraction":
        subtraction(float(x), float(y))
    elif calculation_decision == "multiplication":
        multiplication(float(x), float(y))
    else:
        division(float(x), float(y))
except ValueError:
    print("Please make sure to input addition, subtraction, multiplication, or division and two numbers when prompted!")

