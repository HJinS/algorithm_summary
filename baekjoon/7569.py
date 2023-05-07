import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().rstrip().split(' '))

boxes = [[] for _ in range(H)]

for h in range(H):
    for y in range(N):
        boxes[h].append(list(map(int, sys.stdin.readline().rstrip().split(' '))))


visited = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]


dir_x = [1, -1, 0, 0, 0, 0]
dir_y = [0, 0, 1, -1, 0, 0]

dir_z = [0, 0, 0, 0, 1, -1]
q = deque()


def bfs():
    while q:
        cur_x, cur_y, cur_z = q.popleft()

        for i in range(6):
            n_x = cur_x + dir_x[i]
            n_y = cur_y + dir_y[i]
            n_z = cur_z + dir_z[i]

            if not (0 <= n_x < M and 0 <= n_y < N and 0 <= n_z < H):
                continue
            if visited[n_z][n_y][n_x] > -1 or boxes[n_z][n_y][n_x] == -1:
                continue
            q.append([n_x, n_y, n_z])
            visited[n_z][n_y][n_x] = visited[cur_z][cur_y][cur_x] + 1


for z in range(H):
    for y in range(N):
        for x in range(M):
            if boxes[z][y][x] == 1:
                q.append([x, y, z])
                visited[z][y][x] += 1

bfs()
answer = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if boxes[z][y][x] != -1 and visited[z][y][x] == -1:
                print('-1')
                exit()
            answer = max(answer, visited[z][y][x])

print(answer)
