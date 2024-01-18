import sys


a, b, c = map(int, sys.stdin.readline().rstrip().split(' '))

"""
a ** b

a를 b번 곱해서 c로 나눈 나머지

a를 k번 곱해서 c로 나눈 나머지를 구할 수 있다 -> d
a를 2k번 곱해서 c로 나눈 나머지는 -> d * d % c
a를 k+1번 곱해서 c로 나눈 나머지를 구할 수 있다.
d * a % c
"""
def divide(a, b, c) -> int:
    if b == 1:
        return a * b % c
    result = divide(a, b // 2, c)
    result = result * result % c
    if b % 2 == 1:
        result = result * a % c
    return result

print(divide(a, b, c))
