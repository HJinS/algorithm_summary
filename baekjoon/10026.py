import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

grid = []

for _ in range(N):
    grid.append(list(sys.stdin.readline().rstrip()))

dir_x = [0, 1, 0, -1]
dir_y = [1, 0, -1, 0]

color_blind_mapping = {
    'R': {'R', 'G'},
    'G': {'R', 'G'},
    'B': {'B'}
}

color_normal_mapping = {
    'R': {'R'},
    'G': {'G'},
    'B': {'B'}

}


def bfs(start_x, start_y, mapping, visited):
    q = deque()
    q.append([start_x, start_y])
    start_color = grid[start_y][start_x]
    visited[start_y][start_x] = True

    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            n_x = cur_x + dir_x[i]
            n_y = cur_y + dir_y[i]

            if not (0 <= n_x < N and 0 <= n_y < N):
                continue
            if visited[n_y][n_x] or grid[n_y][n_x] not in mapping[start_color]:
                continue
            q.append([n_x, n_y])
            visited[n_y][n_x] = True


normal_visited = [[False for _ in range(N)] for _ in range(N)]
blind_visited = [[False for _ in range(N)] for _ in range(N)]

normal_count = 0
blind_count = 0

for y in range(N):
    for x in range(N):
        if not normal_visited[y][x]:
            bfs(x, y, color_normal_mapping, normal_visited)
            normal_count += 1
        if not blind_visited[y][x]:
            bfs(x, y, color_blind_mapping, blind_visited)
            blind_count += 1

print(normal_count, blind_count)
