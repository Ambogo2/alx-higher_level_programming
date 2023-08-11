#!/usr/bin/python3
a = 10
b = 5
from calculator_1 import(add, sub, mul, div)

addition = add (a, b)
minus = sub (a, b)
product = mul(a, b)
division = div(a, b)

print(f"{a} + {b} = {addition}")
print(f"{a} - {b} = {minus}")
print(f"{a} * {b} = {product}")
print(f"{a} / {b} = {division}")
