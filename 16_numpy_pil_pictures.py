#!/usr/bin/env python3

# Python 3.9.5

# 16_numpy_read_pictures.py

# Dependencies
import numpy as np
import os
from PIL import Image

# Change working directory to desired location
p = '/Users/user/directory'
os.chdir(p)

# Open and show the image
image = Image.open('sample.png')
image.show()

# Convert the image into a gray colored image:
image = Image.open('sample.png')
img_arary = np.array(image)

# Show array information:
img_arary.shape, img_arary.dtype

# Converting a color image to a grayscale image
gray_img = image.convert("L")
gray_img.show()
