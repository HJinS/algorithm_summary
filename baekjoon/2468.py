from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())

height_map = []

for _ in range(N):
    height_map.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

h_min, h_max = 101, 0

for y in range(N):
    h_min = min(h_min, *height_map[y])
    h_max = max(h_max, *height_map[y])

dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]


def bfs(x, y, height):
    q = deque()
    q.append([x, y])
    visited[y][x] = True

    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            n_x = cur_x + dir_x[i]
            n_y = cur_y + dir_y[i]

            if not (0 <= n_x < N and 0 <= n_y < N) or height_map[n_y][n_x] <= height:
                continue
            if visited[n_y][n_x]:
                continue
            q.append([n_x, n_y])
            visited[n_y][n_x] = True

answer = 1

for height_num in range(h_min, h_max+1):
    safe_count = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    for s_y in range(N):
        for s_x in range(N):
            if not visited[s_y][s_x] and height_map[s_y][s_x] > height_num:
                bfs(s_x, s_y, height_num)
                safe_count += 1
    answer = max(answer, safe_count)
print(answer)
