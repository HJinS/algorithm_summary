import sys
from collections import deque

K = int(sys.stdin.readline().rstrip())

queue = deque()

for _ in range(K):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        queue.pop()
    else:
        queue.append(num)

print(sum(queue))