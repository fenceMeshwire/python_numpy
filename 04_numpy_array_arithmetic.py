#!/usr/bin/env python3

# Python 3.9.7

# 04_numpy_array_arithmetic.py

# Dependencies
import numpy as np

array = np.arange(5)

print('x     = ', array)
print('x + 5 = ', array + 5)
print('x - 5 = ', array - 5)
print('x * 2 = ', array * 2)
print('x / 2 = ', array / 2)
print('x // 2 = ', array // 2) # floor division

print("-x = ", -array)
print("x ** 2 = ", array ** 2)
print("x % 2 = ", array % 2)

-(0.25*array + 2) ** 3

np.add(array, 2)            # Addtion
np.subtract(array, 2)       # Subtraction
np.negative(array)          # Unary negation
np.multiply(array, 2)       # Multiplication
np.divide(array, 2)         # Division
np.floor_divide(array, 2)   # Floor divisioin
np.power(array, 3)          # Exponetiation
np.mod(array, 3)            # Modulus/Remainder
