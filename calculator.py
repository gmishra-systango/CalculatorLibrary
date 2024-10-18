"""
Calculator library containing basic math operations.
"""


def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


# Multiply function
def multiply(first_term, second_term):
    return first_term * second_term


def divide(first_term, second_term):
    try:
        result = first_term / second_term
        return result
    except ZeroDivisionError:
        print("Division by Zero error")
        raise
