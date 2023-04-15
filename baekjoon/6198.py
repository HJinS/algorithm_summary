import sys
from collections import deque
"""
탑 2493이랑 비슷한 류의 문제
생각의 방향만 조금 다름
"""
N = int(sys.stdin.readline().rstrip())
building = deque()

heights = []
for i in range(N):
    heights.append(int(sys.stdin.readline().rstrip()))

count = 0
building.append([N, 1000000001])
for i in range(N-1, -1, -1):
    while building and building[-1][1] < heights[i]:
        building.pop()
    if building:
        count += building[-1][0] - i - 1
    building.append([i, heights[i]])

print(count)
