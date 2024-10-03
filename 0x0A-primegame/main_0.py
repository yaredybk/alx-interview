#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print("Winner: {}".format(isWinner(0, [])))
for i in range(10):
    print("IND: ", i)
    print("Winner: {}".format(isWinner(1, [i])))
