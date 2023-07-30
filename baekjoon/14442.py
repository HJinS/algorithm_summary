import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().rstrip().split(' '))


board = []

for _ in range(N):
    board.append(list(map(int, list(sys.stdin.readline().rstrip()))))


visited = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(K+1)]

dir_x = [0, 1, 0, -1]
dir_y = [1, 0, -1, 0]


def bfs(x, y):
    q = deque()

    q.append([x, y, 0])
    visited[0][y][x] = 1

    while q:
        cur_x, cur_y, break_count = q.popleft()

        for i_x, i_y in zip(dir_x, dir_y):
            n_x = cur_x + i_x
            n_y = cur_y + i_y

            if not (0 <= n_x < M and 0 <= n_y < N):
                continue

            # 벽인 경우
            if board[n_y][n_x] == 1:
                if not 0 <= break_count < K:
                    continue
                if visited[break_count+1][n_y][n_x] >= 0:
                    continue
                q.append([n_x, n_y, break_count+1])
                visited[break_count+1][n_y][n_x] = visited[break_count][cur_y][cur_x] + 1
            else:
                if visited[break_count][n_y][n_x] >= 0:
                    continue

                q.append([n_x, n_y, break_count])
                visited[break_count][n_y][n_x] = visited[break_count][cur_y][cur_x] + 1


bfs(0, 0)
answer = 1000 * 1000 + 1
for i in range(K+1):
    distance = visited[i][N-1][M-1]
    if distance != -1:
        answer = min(visited[i][N-1][M-1], answer)

if answer == 1000 * 1000 + 1:
    print(-1)
else:
    print(answer)
