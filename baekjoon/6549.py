import sys
from collections import deque

while True:
    input_array = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    if input_array[0] == 0 and len(input_array) == 1:
        break
    N, array = input_array[0], input_array[1:]
    stack = deque()
    max_area = 0
    """
    해당 높이가 최초로 나타나기 시작한 위치(해당 높이를 기준으로 직사각형을 만들 수 있는 최초 위치)를 index로 넣음
    나보다 크거나 같은 놈들은 pop하면서 넓이를 계산(현재 스택의 top을 가지고 만들 수 있는 직사각형 넓이 계산)
    스택에는 결국 오름차순으로 들어가게 된다.
    하나씩 pop하면서 넓이를 계산하면 된다. 현재 인덱스 i를 기준으로
    """
    for i in range(N):
        index = i
        while stack and stack[-1][0] >= array[i]:
            max_area = max(max_area, (i - stack[-1][1]) * stack[-1][0])
            index = stack[-1][1]
            stack.pop()
        stack.append([array[i], index])

    """
    스택이 남아 있으면 남아있는 원소들은 전체 길이 N을 기준으로 계산
    """
    while stack:
        max_area = max(max_area, (N - stack[-1][1]) * stack[-1][0])
        stack.pop()
    print(max_area)
