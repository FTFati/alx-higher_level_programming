#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
f = "{:d} ".format(a)
s = " {:d} ".format(b)
print(f + "+" + s + "=" + " {:d}".format(add(a, b)))
print(f + "-" + s + "=" + " {:d}".format(sub(a, b)))
print(f + "*" + s + "=" + " {:d}".format(mul(a, b)))
print(f + "/" + s + "=" + " {:d}".format(div(a, b)))
