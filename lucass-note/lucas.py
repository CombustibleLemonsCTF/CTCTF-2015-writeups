#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# lucas.py


def lucas(n=float('inf')):
    a, b = 2, 1
    if n > 0:
        yield a
    if n > 1:
        yield b
    i = 2
    while i < n:
        a, b, i = b, a + b, i + 1
        yield b


with open('note.txt', 'r') as f:
    data = f.read().strip()
    print('Data size: {} characters'.format(len(data)))

for l in lucas():
    if l > len(data):
        break
    else:
        print(data[l - 1], end='')

print()
