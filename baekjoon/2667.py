import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

house_map = []

for _ in range(N):
    house_map.append(list(map(int, list(sys.stdin.readline().rstrip()))))

visited = [[False for _ in range(N)] for _ in range(N)]
dir_x = [0, 1, 0, -1]
dir_y = [1, 0, -1, 0]


def bfs(x, y, type):
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

            if not (0 <= n_x < N and 0 <= n_y < N) or house_map[n_y][n_x] != type:
                continue
            if visited[n_y][n_x]:
                continue
            q.append([n_x, n_y])
            visited[n_y][n_x] = True
    return count

house_area_count = 0
house_area = []

for y in range(N):
    for x in range(N):
        if not visited[y][x] and house_map[y][x] > 0:
            house_area_count += 1
            house_area.append(bfs(x, y, house_map[y][x]))

print(house_area_count)
house_area = sorted(house_area)
for area in house_area:
    print(area)
