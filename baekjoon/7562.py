from collections import deque
import sys


def bfs(x, y, des_x, des_y):
    q = deque()
    q.append([x, y])
    visited[y][x] += 1
    while q:
        cur_x, cur_y = q.popleft()
        if cur_x == des_x and cur_y == des_y:
            return visited[cur_y][cur_x]
        for i in range(8):
            n_x, n_y = cur_x + dir_x[i], cur_y + dir_y[i]

            if not (0 <= n_x < width and 0 <= n_y < width):
                continue
            if visited[n_y][n_x] >= 0:
                continue
            visited[n_y][n_x] = visited[cur_y][cur_x] + 1
            q.append([n_x, n_y])


dir_x = [2, 1, -2, -1, 2, 1, -2, -1]
dir_y = [1, 2, 1, 2, -1, -2, -1, -2]

test_case_count = int(sys.stdin.readline().rstrip())


for _ in range(test_case_count):
    width = int(sys.stdin.readline().rstrip())
    board = [[0 for _ in range(width)] for _ in range(width)]
    visited = [[-1 for _ in range(width)] for _ in range(width)]
    cur_x, cur_y = map(int, sys.stdin.readline().split(' '))
    des_x, des_y = map(int, sys.stdin.readline().split(' '))

    print(bfs(cur_x, cur_y, des_x, des_y))

