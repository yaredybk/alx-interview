#!/usr/bin/python3
"""N queens.
:q

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
# print("N",N)

def get_queens(test, valid, combo):
    """Find N - 1 non-attacking queens to a queen placed at (x ,y)."""
    # print(test, ":", valid)
    # if test[0] == 0 and test[1] == 1:
        # print(test, valid)
    # if len(valid) > 1 and valid[0][0] == 0 and valid[0][1] == 1:
        # print("TEST",test)
        # print(valid, combo)
    combo[test[0]] = []
    p = test[0] + test[1]
    n = test[0] - test[1]
    tmp_combo = []
    for x_i, tmp in enumerate(combo):
        new_c = [e for e in tmp if test[1] != e and
                 p != (x_i + e) and n != (x_i - e)]
        tmp_combo.append(new_c)
    # combo = tmp_combo

    left = sum([len(tmp) for tmp in tmp_combo])
    valid.append(test)
    # sys.stdout.write(f"...\nV:{valid}\nR:{combo}")
    # sys.stdout.flush()
    if len(valid) == N:
        #if len(valid) > 1 and valid[0][0] == 0 and valid[0][1] == 1:
            # print(test, ":", valid, "!", len(valid))
        return valid
    if left == 0 or left < N - len(valid):
        #if test[0] == 2 and len(valid) > 1 and valid[0][0] == 0 and valid[0][1] == 1:
            # print("left=0 | left < N - valid")
            # print(left, N, len(valid), N - len(valid))
            # print("test", test)
            # print("valid", valid)
            # print("old combo", combo)
            # print("new combo",tmp_combo)
        return None
    combo = tmp_combo
    for x, li in enumerate(combo):
        for y in li:
            q2 = get_queens([x, y], valid[:], combo[:])
            #if test[0] == 0 and test[1] == 1:
                # print([x, y], q2, combo)
            if q2 is not None and len(q2) == N:
                # print(test, ":", q2, "!", len(q2))
                return q2
    #if len(valid) > 0 and valid[0][0] == 0 and valid[0][1] == 1:
        # print(q2, "None")
    return None


if __name__ == "__main__":
    """Check every combination"""
    final = []
    final_set = []
    combo = [list(range(N))] * N
    if N % 2 == 1:
        NN = N + 1
    else:
        NN = N
    for x in range((NN + 1) // 2):
        for y in range((NN + 1) // 2):
            q = get_queens([x, y], [], combo[:])
            if q is not None:
                qq = set([f'{a[0]}{a[1]}' for a in q])
                if qq not in final_set:
                    final_set.append(qq)
                    final.append(q)
                    # sys.stdout.write(f'{str(q)}\n')
                    # sys.stdout.flush()
    [print(a) for a in final]
