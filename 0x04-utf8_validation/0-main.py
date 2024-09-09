#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

def p_v(l):
    print("...")
    print([bin(A) for A in l])
    print(validUTF8(l))


data = [65]
p_v(data)

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
p_v(data)

data = [229, 65, 127, 256]
p_v(data)

p_v([0,1])

p_v([
0b01001000,
0b01010101
    ])


p_v([
0b10000000,
0b01010101
    ])

p_v([
0b11000000,
0b10010101
    ])
p_v([
0b11100000,
0b10110101,
0b10110101
    ])
p_v([
0b11110000,
0b10110101,
0b10010101
    ])
p_v([
0b10000000,
0b01010101,
0b01001000,
0b01010101,
0b01010101,
0b11000000,
0b10010101,
0b11100000,
0b10110101,
0b10110101,
0b11110000,
0b10110101,
0b10010101,
0b10000000,
0b01010101
    ])

p_v([
0b01110011,
0b11101100,
0b10111100,
0b11110100,
    ])
