# Calculator

""""    NOTE:   Since, this is a Basic Level Project,
                The program uses Recursion which forms an infinite loop.
                Terminate the program manually when you don't want to continue any more.
"""

from art import logo

# Add
def add(n1, n2):
    """Add two numbers: n1 + n2"""
    return n1 + n2


# Subtract
def sub(n1, n2):
    """Subtract two numbers: n1 - n2"""
    return n1 - n2


# Multiply
def multiply(n1, n2):
    """Multiply two numbers: n1 * n2"""
    return n1 * n2


# Divide
def divide(n1, n2):
    """Divide two numbers: n1 / n2"""
    return n1 / n2


# Modulus
def mod(n1, n2):
    """Find the remainder of two numbers: n1 % n2"""
    return n1 % n2


# Power
def pow(n1, n2):
    """Exponent of two numbers: n1 ^ n2"""
    return n1 ** n2

# List to store all the operators and their respective functions.
operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide,
    "%": mod,
    "^": pow
}

# Calculator function.
def calculator():
    print(logo)

    # Input number 1.
    num1 = float(input("What's the first number?: "))

    # Print all the operators.
    for symbol in operations:
        print(symbol)

    should_continue = True

    # Continue looping until should_continue is set to False.
    while should_continue:

        # Input an operator.
        operator = input("Pick an operation: ")
        # Input number 2.
        num2 = float(input("What's the next number?: "))

        # Function to be executed = value of operator selected.
        function = operations[operator]
        # Pass the function paramets, i.e, numbers.
        answer = function(num1, num2)
        # Output:
        print(f"{num1} {operator} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        # If user wants to continue, put num1 = previous answer calculated.
        if choice == 'y':
            num1 = answer

        # Else, end the while loop,
        # And start with a new calculation (by using recursion).
        else:
            should_continue = False
            calculator()   # Recursion

# Calling the calculator function.
calculator()
