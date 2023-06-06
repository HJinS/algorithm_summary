import sys
from collections import deque


def init_problem(input_L, input_R, input_C):
    building = []
    for _ in range(input_L):
        floor = []
        for _ in range(input_R):
            floor.append(list(sys.stdin.readline().rstrip()))
        sys.stdin.readline().rstrip()
        building.append(floor)
    return building, [[[-1 for _ in range(input_C)] for _ in range(input_R)] for _ in range(input_L)]


dir_x = [1, 0, -1, 0, 0, 0]
dir_y = [0, 1, 0, -1, 0, 0]
dir_z = [0, 0, 0, 0, 1, -1]


def bfs(s_x, s_y, s_z):
    q = deque()
    q.append([s_x, s_y, s_z])
    visited[s_z][s_y][s_x] += 1

    while q:
        cur_x, cur_y, cur_z = q.popleft()
        if building[cur_z][cur_y][cur_x] == 'E':
            return visited[cur_z][cur_y][cur_x]
        for i in range(6):
            n_x = cur_x + dir_x[i]
            n_y = cur_y + dir_y[i]
            n_z = cur_z + dir_z[i]

            if not (0 <= n_x < C and 0 <= n_y < R and 0 <= n_z < L) or building[n_z][n_y][n_x] == '#':
                continue
            if visited[n_z][n_y][n_x] >= 0:
                continue
            q.append([n_x, n_y, n_z])
            visited[n_z][n_y][n_x] = visited[cur_z][cur_y][cur_x] + 1
    return -1


while True:
    L, R, C = map(int, sys.stdin.readline().rstrip().split(' '))
    if not all([L, R, C]):
        break
    building, visited = init_problem(L, R, C)

    start_point = []
    exit_flag = False
    exit_flag_L = False
    for z in range(L):
        for y in range(R):
            for x in range(C):
                if building[z][y][x] == 'S':
                    start_point = [x, y, z]
                    exit_flag = True
                    break

    result = bfs(*start_point)

    if result == -1:
        print('Trapped!')
    else:
        print(f'Escaped in {result} minute(s).')
