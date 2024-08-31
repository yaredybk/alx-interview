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


def print_s(con: str):
    sys.stdout.write(con)
    sys.stdout.flush()

final_set = []
vv = [[0 for _ in range(N)]] * N
vv2 = [[0 for _ in range(N)]] * N
row_counter = [0 for _ in range(N)]

def get_queens(test, valid, combo, depth):
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
    if left == 0 :
        if len(valid) == N:
            return [valid]
        # global counter
        # counter += 1
        return []
        # REMOVED CONDITION B/C 'neglegible loop count'
    if left < N - len(valid):
        # print("termnated @ ", depth)
        return []
    result = []
    for x, li in enumerate(combo):
        for y in li:
            q2 = get_queens([x, y], valid[:], combo[:], depth + 1)
            for q3 in q2:
                tmp = set([str(a) for a in q3])
                if tmp not in final_set:
                    final_set.append(tmp)
                    result += q2
                    row_counter[valid[0][0]] += 1
                    vv1[valid[0][0]][depth] += 1
                else:
                    vv[valid[0][0]][depth] += 1
                    if row_counter[valid[0][0]] >= N:
                        return result
    return result


if __name__ == "__main__":
    """Check every combination"""
    final = []
    combo = [list(range(N))] * N
    if N % 2 == 1:
        NN = N + 1
    else:
        NN = N
    for x in range(N):
        vv = [[0 for _ in range(N)]] * N
        vv1 = [[0 for _ in range(N)]] * N
        q = get_queens([x, 0], [], combo[:], 0)
        c = 0
        if len(q) > 0:
            for qq in q:
                qqq = set([str(a) for a in qq])
                if qqq not in final_set:
                    final_set.append(qqq)
                    final.append(qq)
                    c += 1
        print_s("--- " + str(x) + " ---\n")
        print("found", c)
        print("empty")
        [print(a) for a in vv]
        print("found")
        [print(a) for a in vv1]

                # else:
                    # counter2 += 1
    # [print(a) for a in final]
    print("NET:",len(final))
    a = [[0 for a in range(N)]] * N
    for ind, l in enumerate(final):
        for x,y in l:
            a[x][y] += 1
    [print(tmp) for tmp in a]
    # global counter
    # print("useless loops",counter)
    # print("similar positions",counter2)
