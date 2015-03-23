#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# solution.py


def decode(encoded):
    decoded = ''
    for index in range(0, len(encoded), 2):
        byte = encoded[index:index + 2]
        decoded += chr(int(bin(int(byte, 16))[2:], 3))
    else:
        return decoded


message_encoded = '27623b1c6b18181fed122b113027111f'
flag_encoded = 'cbcb381b203b232233cbcb'

message, flag = decode(message_encoded), decode(flag_encoded)
print('Message:', message)
print('Flag:', flag)
