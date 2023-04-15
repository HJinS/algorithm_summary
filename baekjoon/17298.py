import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split(' ')))

stack = deque()
answer = [-1] * N
for i in range(N-1, -1, -1):
    while stack and stack[-1] <= array[i]:
        stack.pop()
    if stack:
        answer[i] = stack[-1]
    stack.append(array[i])

print(*answer, end=' ')
