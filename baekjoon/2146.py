from collections import deque
import sys
answer = 100 ** 2 + 1
N = int(sys.stdin.readline().rstrip())

world_map = []

dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]

for _ in range(N):
    world_map.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))


def bfs(x, y, num):
    q = deque()
    q.append([x, y])
    visited[y][x] += 1
    while q:
        cur_x, cur_y = q.popleft()
        world_map[cur_y][cur_x] = num
        for i in range(4):
            n_x = cur_x + dir_x[i]
            n_y = cur_y + dir_y[i]
            if not (0 <= n_x < N and 0 <= n_y < N):
                continue
            if visited[n_y][n_x] >= 0:
                continue
            if world_map[n_y][n_x] == 0:
                continue

            q.append([n_x, n_y])
            visited[n_y][n_x] = visited[cur_y][cur_x] + 1


visited = [[-1 for _ in range(N)] for _ in range(N)]
q = deque()
num = 1
continent_list = []
for y in range(N):
    for x in range(N):
        if visited[y][x] >= 0:
            continue
        if world_map[y][x] == 0:
            continue
        bfs(x, y, num)
        continent_list.append(num)
        num += 1


def bfs2(q):
    global answer
    while q:
        cur_x, cur_y, start_num, count = q.popleft()

        if world_map[cur_y][cur_x] != start_num and world_map[cur_y][cur_x] != 0:
            answer = min(answer, count)
            continue

        for i in range(4):
            n_x = cur_x + dir_x[i]
            n_y = cur_y + dir_y[i]

            if not (0 <= n_x < N and 0 <= n_y < N):
                continue
            if visited2[n_y][n_x] >= 0:
                continue
            if world_map[n_y][n_x] == start_num:
                continue

            q.append([n_x, n_y, start_num, count + 1])
            visited2[n_y][n_x] = visited2[cur_y][cur_x] + 1


for num in continent_list:
    visited2 = [[-1 for _ in range(N)] for _ in range(N)]
    q = deque()
    for y in range(N):
        for x in range(N):
            if world_map[y][x] == 0:
                continue
            if world_map[y][x] == num:
                q.append([x, y, world_map[y][x], 0])
                visited2[y][x] += 1
    bfs2(q)

print(answer - 1)

