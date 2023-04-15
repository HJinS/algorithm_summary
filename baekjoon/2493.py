from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())
tower = deque([])
# 초기값 중요
# 초기값을 큰걸 넣어 그때는 못받는 걸로 처리
tower.append([100000001, 0])
heights = list(map(int, sys.stdin.readline().rstrip().split(' ')))


for i in range(N):
    height = heights[i]
    # 나보다 작은 놈은 뺸다.
    # 나보다 작기 때문 차피 신호 못받음
    while tower[-1][0] < height:
        tower.pop()
    print(tower[-1][1], end=' ')
    tower.append([height, i+1])
