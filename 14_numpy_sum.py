#!/usr/bin/env python3

# Python 3.9.5

# 14_numpy_sum.py

# Dependency
import numpy as np

storage = np.array([[0, 1, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0, 1],
                    [1, 1, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 1, 0, 1, 0],
                    [1, 1, 0, 1, 0, 0],
                    [1, 1, 1, 1, 0, 1]])

# Sum up the values of column 5 and column 6.
# Array starts counting column numbers at 0.
np.sum(storage[:,4] + storage[:,5])

# Sum up the values of the first row
np.sum(storage[:1])
