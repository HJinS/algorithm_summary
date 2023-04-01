import sys

N, X = map(int, sys.stdin.readline().rstrip().split(' '))

arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))


for item in arr:
    if item < X:
        print(item, end=' ')