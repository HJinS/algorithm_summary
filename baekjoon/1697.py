import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split(' '))

directions = [1, -1, 2]

q = deque()
visited = [-1] * 100001

q.append(N)
visited[N] = 0

while q:
    current = q.popleft()

    for direction in directions:
        if abs(direction) == 1:
            n_point = current + direction
        else:
            n_point = current * direction

        if 0 <= n_point <= 100000 and visited[n_point] == -1:
            q.append(n_point)
            visited[n_point] = visited[current] + 1

print(visited[K])
