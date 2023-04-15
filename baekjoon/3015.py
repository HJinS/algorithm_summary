import sys
from collections import deque


N = int(sys.stdin.readline().rstrip())

heights = []
for i in range(N):
    heights.append(int(sys.stdin.readline().rstrip()))

stack = deque()
answer = 0
for i in range(0, N):
    count = 1
    """
    서로 바라 볼 수 있는 사람은 나보다 크거나 같은 사람이다.
    나보다 왼쪽에 있는 사람중 나보다 키가 작은 사람은 스택에서 뺀다(나랑은 볼 수 있지만, 나보다 오른쪽에 있는 사람은 볼 수 없다.)
    나보다 왼쪽에 있는 사람중 나랑 키가 같은 사람은 나의 카운트를 + 1 하고, 스택에서 뺀다.(같은 경우 다음 사람도 확인을 해야 한다(다음 스택) 따라서 뺴고 나의 카운트 + 1) 
    """
    while stack and stack[-1][1] <= heights[i]:
        answer += stack[-1][0]
        if stack[-1][1] == heights[i]:
            count += stack[-1][0]
        stack.pop()
    # 두개가 붙어있는 경우 + 1
    if stack:
        answer += 1
    stack.append([count, heights[i]])

print(answer)
