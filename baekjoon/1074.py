import sys

N, r, c = map(int, sys.stdin.readline().rstrip().split(' '))


def visit_count(n, r, c):
    if n == 1:
        if r == 0 and c == 0:
            return 0
        elif r == 0 and c == 1:
            return 1
        elif r == 1 and c == 0:
            return 2
        elif r == 1 and c == 1:
            return 3

    half = 2 ** (n-1)

    if r < half and c < half:
        result = visit_count(n-1, r, c)
        return result
    elif r < half and c >= half:
        result = visit_count(n-1, r, c - half)
        return result + half ** 2
    elif r >= half and c < half:
        result = visit_count(n-1, r - half, c)
        return result + (half ** 2) * 2
    elif r >= half and c >= half:
        result = visit_count(n-1, r-half, c-half)
        return result + (half ** 2) * 3


print(visit_count(N, r, c))
