#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
print("{} ".format(a) + "+" + " {} ".format(b) + "=" + " {}".format(add(a, b)))
print("{} ".format(a) + "-" + " {} ".format(b) + "=" + " {}".format(sub(a, b)))
print("{} ".format(a) + "*" + " {} ".format(b) + "=" + " {}".format(mul(a, b)))
print("{} ".format(a) + "/" + " {} ".format(b) + "=" + " {}".format(div(a, b)))
