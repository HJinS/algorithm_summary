import sys
from collections import deque


N, M = map(int, sys.stdin.readline().rstrip().split(' '))
iceberg_map = []

dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
max_burg = 0

for _ in range(N):
    input_ice_burg = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    iceberg_map.append(input_ice_burg)
    max_burg = max(max_burg, *input_ice_burg)


def count_sea_area(x, y, iceberg_map):
    sea_area_count = 0
    for dir_idx in range(4):
        next_x = x + dir_x[dir_idx]
        next_y = y + dir_y[dir_idx]
        if 0 <= next_x < M and 0 <= next_y < N and iceberg_map[next_y][next_x] == 0:
            sea_area_count += 1
    return sea_area_count


def bfs(x, y, new_ice_burg_map):
    q = deque()
    q.append([x, y])
    visited[y][x] = True

    while q:
        cur_x, cur_y = q.popleft()
        sea_area = count_sea_area(cur_x, cur_y, iceberg_map)
        new_ice_burg_map[cur_y][cur_x] = max(iceberg_map[cur_y][cur_x] - sea_area, 0)

        for i in range(4):
            n_x = cur_x + dir_x[i]
            n_y = cur_y + dir_y[i]

            if not (0 <= n_x < M and 0 <= n_y < N):
                continue
            if visited[n_y][n_x]:
                continue
            if iceberg_map[n_y][n_x] <= 0:
                continue
            q.append([n_x, n_y])
            visited[n_y][n_x] = True

time = 0

while True:
    if max(max(*iceberg_map)) == 0:
        break
    visited = [[False for _ in range(M)] for _ in range(N)]
    burg_count = 0
    nmw_ice_burg = [[0 for _ in range(M)] for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if visited[y][x]:
                continue
            if iceberg_map[y][x] <= 0:
                continue
            bfs(x, y, nmw_ice_burg)
            burg_count += 1
    if burg_count >= 2:
        print(time)
        sys.exit()

    iceberg_map = nmw_ice_burg
    time += 1

print(0)
