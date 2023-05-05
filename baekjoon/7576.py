import sys
from collections import deque

M, N = map(int, sys.stdin.readline().rstrip().split(' '))

box = []

for _ in range(N):
    box.append(list(map(int, sys.stdin.readline().split(' '))))

Q = deque()
visited = [[-1 for _ in range(M)] for _ in range(N)]
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]


def init_start_point():
    for y in range(N):
        for x in range(M):
            if box[y][x] == 1:
                Q.append([x, y])
                visited[y][x] = 0


def bfs():
    init_start_point()

    while Q:
        cur_x, cur_y = Q.popleft()

        for i in range(4):
            n_x = cur_x + dir_x[i]
            n_y = cur_y + dir_y[i]

            if 0 <= n_x < M and 0 <= n_y < N and visited[n_y][n_x] == -1 and box[n_y][n_x] != -1:
                Q.append([n_x, n_y])
                visited[n_y][n_x] = visited[cur_y][cur_x] + 1

bfs()
answer = 0
for y in range(N):
    for x in range(M):
        if visited[y][x] == -1 and box[y][x] != -1:
            print(-1)
            exit()
        answer = visited[y][x] if answer < visited[y][x] else answer

print(answer)

