import sys
from collections import deque

K = int(sys.stdin.readline().rstrip())

W, H = map(int, sys.stdin.readline().rstrip().split(' '))

world_map = []

for _ in range(H):
    world_map.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))


dir_x1 = [1, 0, -1, 0]
dir_y1 = [0, 1, 0, -1]

dir_x2 = [-2, -1, 2, 1, -2, -1, 2, 1]
dir_y2 = [-1, -2, -1, -2, 1, 2, 1, 2]


visited = [[[-1 for _ in range(W)] for _ in range(H)] for _ in range(K+1)]

"""
2차원만으로는 해결하기 어려울 경우에는 차원을 늘려서 생각하라
말처럼 움직이는 경우와 그냥 움직이는 경우중에서 어느 경우가 더 빨리 갈지는 해봐야 안다.
말처럼 가는 경우는 제한이 있으니, 그걸 기준으로 차원을 늘려서 말처럼 간 횟수마다 카운트를 별도로 한다.
"""


def bfs(K):
    q = deque()
    q.append([0, 0, 0])
    visited[0][0][0] = 0

    while q:
        k, x, y = q.popleft()

        if k < K:
            for d_x, d_y in zip(dir_x2, dir_y2):
                n_x = x + d_x
                n_y = y + d_y

                if not (0 <= n_x < W and 0 <= n_y < H):
                    continue
                if visited[k+1][n_y][n_x] >= 0:
                    continue
                if world_map[n_y][n_x] == 1:
                    continue

                q.append([k+1, n_x, n_y])
                visited[k+1][n_y][n_x] = visited[k][y][x] + 1

        for d_x, d_y in zip(dir_x1, dir_y1):
            n_x = x + d_x
            n_y = y + d_y

            if not (0 <= n_x < W and 0 <= n_y < H):
                continue
            if visited[k][n_y][n_x] >= 0:
                continue
            if world_map[n_y][n_x] == 1:
                continue

            q.append([k, n_x, n_y])
            visited[k][n_y][n_x] = visited[k][y][x] + 1


bfs(K)
answer = 9999999999
for k in range(K+1):
    if visited[k][H-1][W-1] >= 0:
        answer = min(answer, visited[k][H-1][W-1])


if answer != 9999999999:
    print(answer)
else:
    print(-1)
