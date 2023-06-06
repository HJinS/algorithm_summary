import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split(' '))

maze = []

for _ in range(N):
    maze.append(list(map(int, list(sys.stdin.readline().rstrip()))))

dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
visited = [[[-1, -1] for _ in range(M)] for _ in range(N)]


def bfs(x, y):
    q = deque()
    q.append([x, y, 0])
    visited[y][x][0] += 1

    while q:
        cur_x, cur_y, already_broken = q.popleft()
        if cur_x == M-1 and cur_y == N-1:
            if visited[cur_y][cur_x][0] >= 0 and visited[cur_y][cur_x][1] >= 0:
                return min(*visited[cur_y][cur_x])
            elif visited[cur_y][cur_x][0] >= 0:
                return visited[cur_y][cur_x][0]
            elif visited[cur_y][cur_x][1] >= 0:
                return visited[cur_y][cur_x][1]
        for i in range(4):
            n_x = cur_x + dir_x[i]
            n_y = cur_y + dir_y[i]

            if not (0 <= n_x < M and 0 <= n_y < N):
                continue

            """
            벽을 부수는 경우가 아니라면 queue에 넣었던 already_broken을 그대로 visited에 넣어주어야 한다.
            n_x, n_y기준으로 already_broken의 경우에 도달을 하지 않아야한다.
            """
            if maze[n_y][n_x] == 0 and visited[n_y][n_x][already_broken] == -1:
                visited[n_y][n_x][already_broken] = visited[cur_y][cur_x][already_broken] + 1
                q.append([n_x, n_y, already_broken])
            if not already_broken and maze[n_y][n_x] == 1 and visited[n_y][n_x][1] == -1:
                visited[n_y][n_x][1] = visited[cur_y][cur_x][0] + 1
                q.append([n_x, n_y, 1])
    return -1


result = bfs(0, 0)

if result != -1:
    print(result + 1)
else:
    print(-1)
