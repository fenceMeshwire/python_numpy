#!/usr/bin/env python3

# Python 3.9.7

# 12_numpy_aggr_functions.py

# Dependency
import numpy as np

rng = np.random.RandomState(1)

result = []
for intCounter in range(10):
    value = rng.randint(0, 10)
    result.append(value)
print(result)

np.array(result)    # Create an numpy array.

np.sum(result)      # Sum of the elements
np.max(result)      # Maximum of the elements
np.min(result)      # Minimum of the elements
np.prod(result)     # Product of the elements
np.mean(result)     # Mean of the elements
np.std(result)      # Standard variation of the elements
np.var(result)      # Variance of the elements
np.median(result)   # Median of the elements
