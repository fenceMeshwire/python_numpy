#!/usr/bin/env python3

# Python 3.9.7

# 07_numpy_array_split.py

# Dependency
import numpy as np

a = [3, 4, 5, 6, 10, 12, 14, 21, 24, 27]

# Two splitting points [4, 7], three resulting arrays a1, a2, a3
a1, a2, a3 = np.split(a, [4, 7]) 

print(a1)   # [3 4 5 6]
print(a2)   # [10 12 14]
print(a3)   # [21 24 27]

b = np.arange(20)
# Four splitting points [4, 7, 10, 15], five resulting arrays
np.split(b, [4, 7, 10, 15])
