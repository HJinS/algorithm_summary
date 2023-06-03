import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().rstrip().split(' '))

board = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    l_d_x, l_d_y, r_u_x, r_u_y = map(int, sys.stdin.readline().rstrip().split(' '))
    for y in range(l_d_y, r_u_y):
        for x in range(l_d_x, r_u_x):
            board[y][x] = 1

visited = [[False for _ in range(N)] for _ in range(M)]
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]


def print_board():
    for y in range(M):
        for x in range(N):
            print(board[y][x], end=' ')
        print()


def print_visited():
    for y in range(M):
        for x in range(N):
            print(visited[y][x], end=' ')
        print()


def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[y][x] = True
    count = 0
    while q:
        cur_x, cur_y = q.popleft()
        count += 1

        for i in range(4):
            n_x = cur_x + dir_x[i]
            n_y = cur_y + dir_y[i]

            if not (0 <= n_x < N and 0 <= n_y < M) or board[n_y][n_x] == 1:
                continue
            if visited[n_y][n_x]:
                continue
            q.append([n_x, n_y])
            visited[n_y][n_x] = True
    return count


territory_count = 0
territory_area = []


for y in range(M):
    for x in range(N):
        if board[y][x] == 0 and not visited[y][x]:
            territory_count += 1
            territory_area.append(bfs(x, y))

print(territory_count)
print(*(sorted(territory_area)))
