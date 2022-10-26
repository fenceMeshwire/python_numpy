#!/usr/bin/env python3

# Python 3.9.5

# 20_numpy_average.py

# Purpose: Calculate an average price per unit.

# Dependency
import numpy as np

order = [
    {'cat': 1, 'art': 'beer', 'ppu': 4.2, 'cpu': 4.2, 'qty': 1},
    {'cat': 1, 'art': 'water', 'ppu': 1.8, 'cpu': 1.8, 'qty': 1},
    {'cat': 1, 'art': 'water big', 'ppu': 3.0, 'cpu': 3.0, 'qty': 1},
    {'cat': 1, 'art': 'juice', 'ppu': 3.9, 'cpu': 3.9, 'qty': 1},
    {'cat': 1, 'art': 'main dish 1', 'ppu': 13.5, 'cpu': 13.5, 'qty': 1},
    {'cat': 1, 'art': 'main dish 2', 'ppu': 15.5, 'cpu': 15.5, 'qty': 1}
    ]

# ppu: price per unit

ppus = [ppu['ppu'] for ppu in order]
print(ppus) # [4.2, 1.8, 3.0, 3.9, 13.5, 15.5]

average_ppu = np.average(ppus)
print(round(average_ppu, 2)) # 6.98
