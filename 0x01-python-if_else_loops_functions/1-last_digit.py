#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
less = " and is less than 6 and not 0"
great = " and is greater than 5"
if number < 0:
    num = - number
    modulo = num % 10
    dig = - modulo
else:
    dig = number % 10
if dig > 5:
    print("Last digit of " + f"{number:d}" + " is " + f"{dig:d}" + great)
elif dig < 6 and dig != 0:
    print("Last digit of " + f"{number:d}" + " is " + f"{dig:d}" + less)
else:
    print("Last digit of " + f"{number:d}" + " is " + f"{dig:d}" + " and is 0")
