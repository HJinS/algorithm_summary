from collections import deque
import sys

test_case_count = int(sys.stdin.readline().rstrip())

dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]


def bfs_fire():
    while fire_q:
        cur_x, cur_y = fire_q.popleft()
        for i in range(4):
            n_x = cur_x + dir_x[i]
            n_y = cur_y + dir_y[i]

            if not (0 <= n_x < w and 0 <= n_y < h):
                continue
            if fire_visited[n_y][n_x] >= 0:
                continue
            if board[n_y][n_x] == '#':
                continue
            fire_visited[n_y][n_x] = fire_visited[cur_y][cur_x] + 1
            fire_q.append([n_x, n_y])


def bfs_human():
    while human_q:
        cur_x, cur_y = human_q.popleft()
        for i in range(4):
            n_x = cur_x + dir_x[i]
            n_y = cur_y + dir_y[i]

            if not (0 <= n_x < w and 0 <= n_y < h):
                return human_visited[cur_y][cur_x] + 1
            if human_visited[n_y][n_x] >= 0:
                continue
            if fire_visited[n_y][n_x] >= 0 and human_visited[cur_y][cur_x] + 1 >= fire_visited[n_y][n_x]:
                continue
            if board[n_y][n_x] == '#':
                continue
            human_visited[n_y][n_x] = human_visited[cur_y][cur_x] + 1
            human_q.append([n_x, n_y])
    return -1


for _ in range(test_case_count):
    w, h = map(int, sys.stdin.readline().rstrip().split(' '))
    board = []
    fire_visited = [[-1 for _ in range(w)] for _ in range(h)]
    human_visited = [[-1 for _ in range(w)] for _ in range(h)]
    human_q = deque()
    fire_q = deque()

    for _ in range(h):
        board.append(sys.stdin.readline().rstrip())

    for y in range(h):
        for x in range(w):
            if board[y][x] == '*':
                fire_q.append([x, y])
                fire_visited[y][x] += 1
            elif board[y][x] == '@':
                human_q.append([x, y])
                human_visited[y][x] += 1
    bfs_fire()
    result = bfs_human()
    if result == -1:
        print('IMPOSSIBLE')
    else:
        print(result)