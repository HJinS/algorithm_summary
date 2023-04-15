from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())

queue = deque([i for i in range(N, 0, -1)])

while len(queue) >= 2:
    queue.pop()
    num = queue.pop()
    queue.appendleft(num)

print(queue[0])