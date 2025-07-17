#!/usr/bin/env python3

# Calculator -- a four function calculator command line tool

# -------------------------------------------------------- #
# -- CALCULATOR FUNCTIONS -------------------------------- #
# -------------------------------------------------------- #

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

# -------------------------------------------------------- #
# -- MAIN FUNCTIONALITY ---------------------------------- #
# -------------------------------------------------------- #

while True:
    try:
        a = int(input("Enter the first argument: "))
        op = input("Enter the operation (+, -, *, /): ")
        b = int(input("Enter the second argument: "))

        if op == "+":
            print("Sum:", add(a, b))
        elif op == "-":
            print("Difference:", sub(a, b))
        elif op == "*":
            print("Product:", mult(a, b))
        elif op == "/":
            print("Quotient:", div(a, b))
        else:
            print("Invalid operation...")

    except ValueError:
        print("Invalid number argument...")

    q = input("Quit? [y/n]: ")
    if q.lower() == "y":
        break
