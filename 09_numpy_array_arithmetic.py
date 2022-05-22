#!/usr/bin/env python3

# Python 3.9.7

# 09_numpy_array_arithmetic.py

# Dependency
import numpy as np

array = np.arange(5)

# Basic numpy operations:
np.add(array, 2)            # Addtion
np.subtract(array, 2)       # Subtraction
np.negative(array)          # Unary negation
np.multiply(array, 2)       # Multiplication
np.divide(array, 2)         # Division
np.floor_divide(array, 2)   # Floor divisioin
np.power(array, 3)          # Exponetiation
np.mod(array, 3)            # Modulus/Remainder

# Absolute value:
array = np.array([-5, -4, -3, -2, -1])
abs(array)
np.absolute(array)
np.abs(array)

# Calculation is also possible:
print('x      = ', array)
print('x + 4  = ', array + 4)
print('x - 6  = ', array - 6)
print('x * 3  = ', array * 3)
print('x / 4  = ', array / 4)
print('x // 3 = ', array // 3)

print("-x = ", -array)
print("x ** 2 = ", array ** 2)
print("x % 2 = ", array % 2)

# Written as a function:
-(0.125 * array + 4) ** 5
