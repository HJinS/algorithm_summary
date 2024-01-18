import sys


"""
k개를 a -> b로 옮길 수 있다면
K+1을 a -> c로 옮길 수 있다.

k개를 a -> b
1개를 a -> c
k개를 b -> c

1 -> 1
2 -> 3
3 -> 7


2**k- 1
2 - 1
"""



sys.setrecursionlimit(30000)


def hanoi(a, b, k):
    """
    k개를 a에서 b로 옮기는 것
    """
    if k == 1:
        print(f'{a} {b}')
        return

    hanoi(a, 6 - (a+b), k-1)
    print(f'{a} {b}')
    hanoi(6 - (a + b), b, k - 1)


k = int(input())
count = (2 ** k - 1) / (2 - 1)
print(int(count))
hanoi(1, 3, k)
