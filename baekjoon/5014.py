import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().rstrip().split(' '))

dir = [U, -1*D]

visited = [-1 for _ in range(1000001)]


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] += 1
    while q:
        cur = q.popleft()

        if cur == G:
            return visited[cur]
        for i in range(2):
            n = cur + dir[i]

            if not (1 <= n <= F):
                continue
            if visited[n] >= 0:
                continue
            visited[n] = visited[cur] + 1
            q.append(n)
    return -1


answer = bfs(S)
if answer == -1:
    print('use the stairs')
else:
    print(answer)