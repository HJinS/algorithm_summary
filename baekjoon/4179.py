import sys
from collections import deque


R, C = map(int, sys.stdin.readline().rstrip().split(' '))

maze = []

for _ in range(R):
    maze.append(list(sys.stdin.readline().rstrip()))

dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]

human_visited = [[-1 for _ in range(C)] for _ in range(R)]
fire_visited = [[-1 for _ in range(C)] for _ in range(R)]
fire_q = deque()
human_q = deque()


def fire_bfs():
    while fire_q:
        cur_x, cur_y = fire_q.popleft()
        
        for i in range(4):
            n_x = cur_x + dir_x[i]
            n_y = cur_y + dir_y[i]

            if not (0 <= n_x < C and 0 <= n_y < R):
                continue
            if fire_visited[n_y][n_x] >= 0 or maze[n_y][n_x] == '#':
                continue
            fire_q.append([n_x, n_y])
            fire_visited[n_y][n_x] = fire_visited[cur_y][cur_x] + 1


def human_bfs():
    while human_q:
        cur_x, cur_y = human_q.popleft()

        for i in range(4):
            n_x = cur_x + dir_x[i]
            n_y = cur_y + dir_y[i]

            if not (0 <= n_x < C and 0 <= n_y < R):
                print(human_visited[cur_y][cur_x] + 1)
                exit()
            if human_visited[n_y][n_x] >= 0 or maze[n_y][n_x] == '#':
                continue
            if fire_visited[n_y][n_x] != -1 and fire_visited[n_y][n_x] <= human_visited[cur_y][cur_x] + 1:
                continue
            human_q.append([n_x, n_y])
            human_visited[n_y][n_x] = human_visited[cur_y][cur_x] + 1


human_start, fire_start = None, None


for y in range(R):
    for x in range(C):
        if maze[y][x] == 'F':
            fire_q.append([x, y])
            fire_visited[y][x] = 0
        if maze[y][x] == 'J':
            human_q.append([x, y])
            human_visited[y][x] = 0


def print_visited(visited):
    for _ in range(R):
        print(*visited[_])



fire_bfs()
human_bfs()
print('IMPOSSIBLE')
