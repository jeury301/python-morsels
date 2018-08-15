from math import sqrt

def v0_is_perfect_square(number):
    """Return True if given number is the square of an integer."""
    return int(number**0.5)**2 == number

def v1_is_perfect_square(number):
    """Return True if given number is the square of an integer."""
    return int(sqrt(number))**2 == number

def v2_is_perfect_square(number):
    """Return True if given number is the square of an integer."""
    return sqrt(number) == int(sqrt(number))

def v3_is_perfect_square(number):
    """Return True if given number is the square of an integer."""
    # checks for intger-ness
    return sqrt(number) % 1 == 0

def v4_is_perfect_square(number):
    """Return True if given number is the square of an integer."""
    return sqrt(number).is_integer()

def v5_is_perfect_square(number):
    """Return True if given number is the square of an integer.

    Bonus 1: Handle negative numbers
    """
    if number < 0:
        return False
    return sqrt(number).is_integer()

def v6_is_perfect_square(number):
    """Return True if given number is the square of an integer."""
    try:
        return sqrt(number).is_integer()
    except ValueError:
        return False

from decimal import Decimal

def v7_is_perfect_square(number):
    """Return True if given number is the square of an integer.

    Bonus 2: Support large numbers
    """
    return int(Decimal(number).sqrt())**2 == number

from decimal import Context, Decimal, localcontext

def v8_is_perfect_square(number):
    """Return True if given number is the square of an integer."""
    digit_count = len(str(number))
    with localcontext(Context(prec=digit_count*2)):
        return int(Decimal(number).sqrt())**2 == number

def v9_is_perfect_square(number):
    """Return True if given number is the square of an integer."""
    if number < 0:
        return False
    digit_count = len(str(number))
    with localcontext(Context(prec=digit_count*2)):
        return int(Decimal(number).sqrt())**2 == number

import cmath

def is_perfect_square(number, *, complex=False):
    """Return True if given number is the square of an integer.

    Bonus 3: Checking for complex sqaure numbers
    """
    if complex:
        root = cmath.sqrt(number)
        return root.real.is_integer() and root.imag.is_integer()
    if number < 0:
        return False
    digit_count = len(str(number))
    with localcontext(Context(prec=digit_count*2)):
        return int(Decimal(number).sqrt())**2 == number
