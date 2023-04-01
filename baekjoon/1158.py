import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split(' '))

deq = deque([i for i in range(1, N+1)])

count = 0

answer = []

while deq:
    first = deq.popleft()
    count += 1
    if count == K:
        count = 0
        answer.append(first)
    else:
        deq.append(first)

print('<', end='')
for index, num in enumerate(answer):
    if index == N-1:
        print(f'{num}>', end='')
    else:
        print(f'{num}, ', end='')

