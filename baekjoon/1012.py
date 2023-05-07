import sys
from collections import deque

total_test_case = int(sys.stdin.readline().rstrip())
dir_x = [0, 1, 0, -1]
dir_y = [1, 0, -1, 0]


def bfs(start_x, start_y, visited, n, m, board):
    q = deque()
    q.append([start_x, start_y])
    visited[start_y][start_x] = True
    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            n_x = cur_x + dir_x[i]
            n_y = cur_y + dir_y[i]

            if not (0 <= n_x < m and 0 <= n_y < n):
                continue
            if visited[n_y][n_x] or board[n_y][n_x] == 0:
                continue
            q.append([n_x, n_y])
            visited[n_y][n_x] = True


def print_visited(n, visited):
    for _ in range(n):
        print(*visited[_])


for _ in range(total_test_case):
    M, N, K = map(int, sys.stdin.readline().rstrip().split(' '))
    board = [[0 for _ in range(M)] for _ in range(N)]
    answer = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().rstrip().split(' '))
        board[y][x] = 1

    for y in range(N):
        for x in range(M):
            if not visited[y][x] and board[y][x] == 1:
                bfs(x, y, visited, N, M, board)
                answer += 1
    print(answer)

