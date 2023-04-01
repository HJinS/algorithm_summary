import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))
X = int(sys.stdin.readline().rstrip())

check_set = set()
cnt = 0
for item in arr:
    diff = X - item
    if diff in check_set:
        cnt += 1
    check_set.add(item)

print(cnt)