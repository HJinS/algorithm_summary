import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split(' '))

maze = []

for _ in range(N):
    maze.append(list(map(int, list(sys.stdin.readline().rstrip()))))
    
visited = [[-1 for _ in range(M)] for _ in range(N)]
dir_x = [0, 1, 0, -1]
dir_y = [1, 0, -1, 0]


def bfs(start_x, start_y, target_x, target_y):
    Q = deque()
    Q.append([start_x, start_y])
    visited[start_y][start_x] = 1
    
    while Q:
        cur_x, cur_y = Q.popleft()
        if cur_x == target_x and cur_y == target_y:
            return visited[cur_y][cur_x]
        for i in range(4):
            n_x = cur_x + dir_x[i]
            n_y = cur_y + dir_y[i]
            if 0 <= n_x < M and 0 <= n_y < N and maze[n_y][n_x] == 1 and visited[n_y][n_x] == -1:
                Q.append([n_x, n_y])
                visited[n_y][n_x] = visited[cur_y][cur_x] + 1
    return 0


print(bfs(0, 0, M-1, N-1))
