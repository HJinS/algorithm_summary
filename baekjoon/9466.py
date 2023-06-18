import sys
from collections import deque

test_case = int(sys.stdin.readline().rstrip())

"""
틀림
"""

NOT_VISITED = 0
CYCLE_IN = -1


def run(point):
    cur = point
    while True:
        state[cur] = point
        cur = choices[cur]
        # 처음 시작점일 경우, 싸이클인 경우
        if state[cur] == point:
            while state[cur] != CYCLE_IN:
                state[cur] = CYCLE_IN
                cur = choices[cur]
            return None
        # 처음 시작점이 아니지만 이미 방문한 곳일 경우
        elif state[cur] != 0:
            return None
"""
BFS라기보다는 단순 구현 문제에 가깝다
싸이클을 판별하는게 중요
방문 안한 상태와 싸이클인 상태를 구분하는게 중요
싸이클을 발견 한 경우 while문으로 선택을 따라 싸이클임을 표시
방문 했고, 싸이클이 아닌 경우는 선택한 겂 입력
"""

for _ in range(test_case):
    student_count = int(sys.stdin.readline().rstrip())
    choices = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    choices.insert(0, 0)
    total_team_count = 0

    state = [0 for _ in range(student_count+1)]

    for student in range(1, student_count+1):
        if state[student] == NOT_VISITED:
            run(student)

    for student in range(1, student_count+1):
        if state[student] != CYCLE_IN:
            total_team_count += 1
    print(total_team_count)
