#!/usr/bin/python3
"""N queens.

prints the positions of
N non-attacking queens on an N×N chessboard

Where:
    N is command line argument
    
example:
    >>> ./0-nqueens 4
    [[1, 0], [0, 2], [2, 3], [3, 1]]
    [[2, 0], [0, 1], [1, 3], [3, 2]]
"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
N = sys.argv[1]
try:
    N = int(N)
except ValueError:
    print("N must be a number")
    sys.exit(1)
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

checker = []
result = []


def get_queens(test, valid, combo):
    """Find N - 1 non-attacking queens to a queen placed at (x, y).
    
    results are appended to global result variable
    """
    # remove vertical line of attack
    combo[test[0]] = []
    # find offset for diagonal attack
    p = test[0] + test[1]
    n = test[0] - test[1]
    tmp_combo = []
    # remove horizontal and diagonal line of attack
    for x_i, tmp in enumerate(combo):
        new_c = [y for y in tmp if test[1] != y and
                 p != (x_i + y) and n != (x_i - y)]
        tmp_combo.append(new_c)
    combo = tmp_combo
    valid.append(test)
    remaining = sum([len(tmp) for tmp in combo])
    if len(valid) == N:
        tmp = set([str(a) for a in valid])
        if tmp not in checker:
            checker.append(tmp)
            result.append(valid)
        return None

    if remaining == 0 or remaining < N - len(valid):
        return None

    for x, li in enumerate(combo):
        for y in li:
            get_queens([x, y], valid[:], combo[:])


if __name__ == "__main__":
    """Check every combination"""
    combo = [list(range(N))] * N
    if N % 2 == 1:
        NN = N + 1
    else:
        NN = N
    for x in range(N):
        get_queens([x, 0], [], combo[:])

    [print(a) for a in result]
    # print(len(result))
    # global counter
    # print("useless loops",counter)
    # print("similar positions",counter2)
