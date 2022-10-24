#!/usr/bin/env python3

# Python 3.9.5

# 18_numpy_array_element_diff.py

# Dependency
import numpy as np

# Given sequence of numbers
numbers = np.array([7, 5, 1, 3, 0, 7 ,2, 3, 0, 8, 4, 4, 0, 8, 5, 7])

# Calculate the difference from one number to the next
diff_numbers = np.diff(numbers)

print(diff_numbers) # [-2 -4  2 -3  7 -5  1 -3  8 -4  0 -4  8 -3  2]

print(diff_numbers[::2]) # print every second element
print(diff_numbers[::3]) # print every third element

for i in range(1, 9):
    print(diff_numbers[::i])
