import sys

N = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))
v = int(sys.stdin.readline().rstrip())

count = 0
for num in arr:
    if v == num:
        count += 1

print(count)