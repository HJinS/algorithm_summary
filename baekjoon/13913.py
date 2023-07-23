import sys
from collections import deque


N, K = map(int, sys.stdin.readline().rstrip().split(' '))


directions = [2, -1, 1]
visited = [-1 for _ in range(100002)]

pre_position = [-1 for _ in range(100002)]
answer_path = deque()

def bfs(N, K):
    q = deque()

    q.append(N)
    visited[N] = 0

    while q:
        current = q.popleft()
        if current == K:
            while current != N:
                answer_path.append(current)
                current = pre_position[current]
            answer_path.append(current)
            return visited[K]
        for direction in directions:
            if direction == 2:
                next_cur = current * direction
            else:
                next_cur = current + direction

            if not (0 <= next_cur <= 100000):
                continue

            if visited[next_cur] >= 0:
                continue

            visited[next_cur] = visited[current] + 1

            """
            path를 string으로 queue에 넣으면 용량이 너무 커진다.
            문자열 계산이 느리다
            """
            pre_position[next_cur] = current
            q.append(next_cur)


time = bfs(N, K)
print(time)
for _ in range(len(answer_path)-1, 0, -1):
    print(answer_path[_], end=' ')

print(answer_path[0])