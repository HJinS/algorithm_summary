import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split(' '))


"""
-1 먼저
4 6 일경우
4 -> 3 -> 6

순간이동 하는 경우가 최우선(비용이 들지 않음)
-1 하는 경우가 2번째 우선(-1했을 경우 순간이동으로 정답으로 갈 수도 있음)
"""
directions = [2, -1, 1]
visited = [-1 for _ in range(200000)]


def bfs(N):
    global visited
    q = deque()
    q.append(N)
    visited[N] = 0
    while q:
        current_position = q.popleft()
        for i in range(3):
            """
            순간이동을 하는 경우는 appendleft하는 것이 중요
            순간이동은 비용이 안들기 때문
            """
            if directions[i] == 2:
                next_position = current_position * directions[i]
                """
                순간이동의 경우에는 position이 0인 경우도 허용해 줘야 함
                """
                if not (next_position < 200000):
                    continue
                if visited[next_position] != -1:
                    continue
                q.appendleft(next_position)
                visited[next_position] = visited[current_position]
            else:
                next_position = current_position + directions[i]
                if not (0 <= next_position < 200000):
                    continue
                if visited[next_position] != -1:
                    continue
                q.append(next_position)
                visited[next_position] = visited[current_position] + 1


bfs(N)
print(visited[K])
