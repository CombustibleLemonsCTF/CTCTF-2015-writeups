#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# solution.py


import imagelib


filename = 'barcode.ppm'

print('Reading image from {} . . . '.format(filename))
image = imagelib.read_image(filename)
height, width = image.shape[:2]
print('Image dimensions: {} x {} pixels'.format(height, width))

row = image[height - 1]
for x, pixel in enumerate(row):
    if tuple(pixel) != (0, 0, 0):
        for y in range(height):
            image[y, x] = (0, 0, 0)
    else:
        for y in range(height):
            image[y, x] = (255, 255, 255)

print('Writing image to tmp.ppm . . . ')
imagelib.write_image('tmp.ppm', image)
