#!/usr/bin/env python3

# Python 3.9.7

# 06_numpy_array_concatenation.py

# Dependency
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])

np.concatenate([a, b])

np.concatenate([a, b, c])

sample = np.array([[3, 2, 5], 
                   [4, 5, 8]])

# Concatenate along the first axis (downwards, axis=0)
np.concatenate([sample, sample]) 

# Concatenate along the second axis (to the right, axis=1)
np.concatenate([sample, sample], axis=1)
