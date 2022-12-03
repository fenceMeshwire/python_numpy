#!/usr/bin/env python3

# Python 3.9.5

# 21_numpy_data_type_conversion.py

# Dependency
import numpy as np

# Values are available in a list of strings and converted into the data type float:
strings = np.array(['25', '9.81', '71', '3.14159', '109'], dtype=np.string_)
floats = strings.astype(float)

floats.dtype    # dtype('float64')
print(floats)
