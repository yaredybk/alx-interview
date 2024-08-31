#!/usr/bin/python3
"""N queens.

using backtracking.
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
# only for performace tests
# counter = 0
# counter2 = 0


def get_queens(test, valid, combo):
    """Find N - 1 non-attacking queens to a queen placed at (x, y).

    Returns:
        Nested list of non-attacking queen's position
        example:
            [[0, 0], [1, 2], [2, 4], [3, 1], [4, 3]]
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
    left = sum([len(tmp) for tmp in combo])
    if left == 0:
        # REMOVED CONDITION B/C 'neglegible loop count'
        # or left < N - len(valid):
        if len(valid) == N:
            return [valid]
        # global counter
        # counter += 1
        return []
    result = []
    for x, li in enumerate(combo):
        for y in li:
            q2 = get_queens([x, y], valid[:], combo[:])
            if len(q2) > 0:
                result += q2
    return result


if __name__ == "__main__":
    """Check every combination"""
    final = []
    final_set = []
    combo = [list(range(N))] * N
    if N % 2 == 1:
        NN = N + 1
    else:
        NN = N
    for x in range(N):
        q = get_queens([x, 0], [], combo[:])
        if len(q) > 0:
            for qq in q:
                qqq = set([str(a) for a in qq])
                if qqq not in final_set:
                    final_set.append(qqq)
                    final.append(qq)
                # else:
                    # counter2 += 1

    [print(a) for a in final]
    # print(len(final))
    # global counter
    # print("useless loops",counter)
    # print("similar positions",counter2)
