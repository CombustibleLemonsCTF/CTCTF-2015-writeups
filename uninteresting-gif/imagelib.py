#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# machine-vision/imagelib.py


import numpy as np


def read_image(filename):
    with open(filename, 'r') as image_file:
        raw_data = image_file.read().strip().split()
    
    signature = raw_data[0]
    assert signature == 'P3', 'Invalid file signature.'
    width, height = int(raw_data[1]), int(raw_data[2])
    assert 4 + 3 * width * height == len(raw_data), 'Missing or extra data.'
    max_value = int(raw_data[3])
    assert max_value == 255, 'Unhandled maximum value.'
    raw_data = raw_data[4:]
    
    generator = (int(value) for value in raw_data)
    return np.fromiter(generator, np.uint8).reshape(height, width, 3)


def write_image(filename, image):
    with open(filename, 'w+') as image_file:
        image_file.write('P3\n')
        image_file.write('{1} {0}\n'.format(*image.shape))
        image_file.write('255\n')
        
        for row in image:
            for pixel in row:
                image_file.write('{} {} {}\n'.format(*pixel))


def blank_image(height, width, color=(255, 255, 255)):
    return np.array(color * height * width, np.uint8).reshape(height, width, 3)


def line(height, width, m, b):
    if abs(m) > 1:
        for y in range(height):
            x = int(round((y - b) / m))
            if 0 <= x < width:
                yield x, y
    else:
        for x in range(width):
            y = int(round(m * x + b))
            if 0 <= y < height:
                yield x, y
