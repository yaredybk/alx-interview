#!/usr/bin/python3
"""
Test the function minOperations
"""


minOperations = __import__('0-minoperations').minOperations

def tmp_func (n):
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

tmp_func(0)
tmp_func(1)
tmp_func(2)
tmp_func(3)
tmp_func(4)
tmp_func(12)
tmp_func(50)
tmp_func(211)
tmp_func(213)
tmp_func(301)
tmp_func(601)
