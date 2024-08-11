#!/usr/bin/python3
"""
Test the function minOperations
"""


minOperations = __import__('0-minoperations').minOperations
minOperations2 = __import__('test1').minOperations

def tmp_func (n):
    print("Min # of operations1 to reach {} char: {}".format(n, minOperations(n)))
    print("Min # of operations2 to reach {} char: {}".format(n, minOperations2(n)))

tmp_func(7079)
#tmp_func(0)
#tmp_func(1)
#tmp_func(2)
#tmp_func(3)
#tmp_func(4)
#tmp_func(12)
#tmp_func(17)
#tmp_func(50)
#tmp_func(211)
#tmp_func(213)
#tmp_func(301)
#tmp_func(601)
#tmp_func(12345678)
#tmp_func(6015556654)
#tmp_func(6015556611)
#tmp_func(6015000000)
tmp_func(10000019)
tmp_func(10000020)
tmp_func(57599)
