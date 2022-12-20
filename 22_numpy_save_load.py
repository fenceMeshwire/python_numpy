#!/usr/bin/env python3

# Python 3.9.5

# 22_numpy_save_load.py

# Dependencies
import numpy as np
import os, platform
from pathlib import Path

if os.name == 'nt' or platform.system() == 'Windows':
    path = 'C:\\...'
    os.chdir(path)
if os.name == 'posix' or platform.system() == 'Darwin':
    path = '/Users/...'
    os.chdir(path)

print('Path changed to:', Path.cwd())

# Create a numpy array:
data = np.arange(20)

# Save data:
np.save('numpy_data', data)

# Load data:
np.load('numpy_data.npy')

# Save to archive:
np.savez('data_archive.npz', a=data, b=data)

# Return data:
data_archived = np.load('data_archive.npz')
data_archived['b']

# Save compressed data
np.savez_compressed('data_compressed.npz', a=data, b=data)
