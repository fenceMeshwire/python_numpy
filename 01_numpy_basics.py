#!/usr/bin/env python3

# Python 3.9.7

# 01_numpy_basics.py

# Dependency
import numpy as np

np.random.seed(10) # seed for reproducibility

a = np.random.randint(10, size=4) # One-dimensional array
b = np.random.randint(10, size=(2, 3)) # Two-dimensional array
c = np.random.randint(10, size=(2, 3, 4)) # Three-dimensional array

a # Returns array values, e.g. array([9, 4, 0, 1])
b # Returns array values, e.g. array([...])
c # Returns array values, e.g. array([[...], [...])

print('Parameter c ndim: ', c.ndim)
print('Parameter c shape: ', c.shape)
print('Parameter c size: ', c.size)

print('Parameter dtype:', c.dtype)
print('Parameter itemsize:', c.itemsize, 'bytes')
print('Parameter nbytes:', c.nbytes, 'bytes')
