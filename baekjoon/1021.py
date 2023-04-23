import sys
from collections import deque
from typing import Optional


def find(deq: deque, num: int) -> Optional[int]:
    for idx, item in enumerate(deq):
        if item == num:
            return idx
    return None

N, M = map(int, sys.stdin.readline().rstrip().split(' '))
arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))
deq = deque([i for i in range(1, N+1)])
"""
해당 원소가 deque에서 어디에 있는지 위치를 알아야 한다.
그 위치를 기준으로 중앙에서 왼쪽인지 오른쪽인지에 따라 pop 및 push의 방향을 결정한다.
"""
count = 0
for num in arr:
    if len(deq) % 2 == 0:
        head, tail = len(deq) // 2 - 1, len(deq) // 2
    else:
        head, tail = len(deq) // 2, len(deq) // 2
    idx = find(deq, num)
    if idx <= head:
        while deq[0] != num:
            item = deq.popleft()
            deq.append(item)
            count += 1
    else:
        while deq[0] != num:
            item = deq.pop()
            deq.appendleft(item)
            count += 1
    deq.popleft()
    if len(deq) % 2 == 0:
        head, tail = len(deq) // 2 - 1, len(deq) // 2
    else:
        head, tail = len(deq) // 2, len(deq) // 2


print(count)