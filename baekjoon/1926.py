import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split(' '))
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))


dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]

visited = [[False for _ in range(M)] for _ in range(N)]


def bfs(start_x, start_y):
    Q = deque()
    area = 0
    Q.append([start_x, start_y])
    visited[start_y][start_x] = True
    while Q:
        cur_x, cur_y = Q.popleft()
        area += 1
        for i in range(4):
            n_x = cur_x + dir_x[i]
            n_y = cur_y + dir_y[i]

            if 0 <= n_x < M and 0 <= n_y < N and not visited[n_y][n_x] and board[n_y][n_x] == 1:
                Q.append([n_x, n_y])
                visited[n_y][n_x] = True
    return area


max_area = 0
paint_count = 0

for y in range(N):
    for x in range(M):
        if not visited[y][x] and board[y][x] == 1:
            area = bfs(x, y)
            max_area = max(max_area, area)
            paint_count += 1

print(paint_count)
print(max_area)

