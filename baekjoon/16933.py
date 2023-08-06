import sys
from collections import deque


N, M, K = map(int, sys.stdin.readline().rstrip().split(' '))

board = []

for _ in range(N):
    board.append(list(map(int, list(sys.stdin.readline().rstrip()))))

dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]

visited = [[[[-1 for _ in range(M)] for _ in range(N)] for _ in range(K+1)] for _ in range(2)]


def bfs():

    """
    머무르는지의 여부는 밤인가 낮인가의 여부로 결정한다(1 혹은 0)
    밤인지, 낮인지, 벽 부순 횟수, y, x 기준으로 배열을 만든다(머무르는 횟수는 상관 없음)

    벽 부수는 횟수에 대한 continue는 앞에(쓸대없이 머무르는 것을 막기 위함)

    time out ㅡ.ㅡ
    """
    q = deque()
    visited[0][0][0][0] = 1

    q.append([0, 0, 0, 0])

    while q:
        cur_x, cur_y, is_night, break_count = q.popleft()

        if cur_x == M-1 and cur_y == N-1:
            print(visited[is_night][break_count][cur_y][cur_x])
            return

        for n_dir_x, n_dir_y in zip(dir_x, dir_y):
            n_x = cur_x + n_dir_x
            n_y = cur_y + n_dir_y

            if not (0 <= n_y < N and 0 <= n_x < M):
                continue

            if board[n_y][n_x] == 1:
                if break_count == K:
                    continue

                if not is_night:
                    if visited[1-is_night][break_count+1][n_y][n_x] > 0:
                        continue
                    visited[1-is_night][break_count+1][n_y][n_x] = visited[is_night][break_count][cur_y][cur_x] + 1
                    q.append([n_x, n_y, 1-is_night, break_count+1])
                else:
                    if visited[1-is_night][break_count][cur_y][cur_x] > 0:
                        continue
                    visited[1-is_night][break_count][cur_y][cur_x] = visited[is_night][break_count][cur_y][cur_x] + 1
                    q.append([cur_x, cur_y, 1-is_night, break_count])

            else:
                if visited[1-is_night][break_count][n_y][n_x] > 0:
                    continue
                visited[1-is_night][break_count][n_y][n_x] = visited[is_night][break_count][cur_y][cur_x] + 1
                q.append([n_x, n_y, 1-is_night, break_count])


bfs()
