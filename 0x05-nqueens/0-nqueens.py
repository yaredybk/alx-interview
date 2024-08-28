#!/usr/bin/python3
"""N queens.

using backtracking.
"""
import sys


if len(sys.argv) != 2:
    sys.stdout.write("Usage: nqueens N")
    sys.stdout.flush()
    sys.exit(1)
N = sys.argv[1]
try:
    N = int(N)
except ValueError:
    sys.stdout.write("N must be a number")
    sys.stdout.flush()
    sys.exit(1)
if N < 4:
    sys.stdout.write("N must be at least 4")
    sys.stdout.flush()
    sys.exit(1)


def get_queens(test, valid, combo):
    """Find N - 1 non-attacking queens to a queen placed at (x ,y)."""
    combo[test[0]] = []
    p = test[0] + test[1]
    n = test[0] - test[1]
    tmp_combo = []
    for x_i, tmp in enumerate(combo):
        new_c = [e for e in tmp if test[1] != e and
                 p != (x_i + e) and n != (x_i - e)]
        tmp_combo.append(new_c)
    combo = tmp_combo

    left = sum([len(tmp) for tmp in combo])
    valid.append(test)
    # sys.stdout.write(f"...\nV:{valid}\nR:{combo}")
    # sys.stdout.flush()
    if len(valid) == N:
        return valid
    if left == 0 or left < N - len(valid):
        return None
    for x, li in enumerate(combo):
        for y in li:
            q2 = get_queens([x, y], valid[:], combo[:])
            if q2 is not None and len(q2) == N:
                return q2
    return None


if __name__ == "__main__":
    """Check every combination"""
    final = []
    combo = [list(range(N))] * N
    if N % 2 == 1:
        N += 1
    for x in range(N):
        a = min(x + 1, (N - x))
        for y in range(a):
            q = get_queens([y, x], [], combo[:])
            if q is not None:
                qq = set([f'{a[0]}{a[1]}' for a in q])
                if qq not in final:
                    final.append(qq)
                    sys.stdout.write(f'{str(q)}\n')
                    sys.stdout.flush()
