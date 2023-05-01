from collections import deque
import sys

N, L = map(int, sys.stdin.readline().rstrip().split(' '))

A = list(map(int, sys.stdin.readline().rstrip().split(' ')))

deq = deque()
answer = []

for i in range(N):
    start, end = max(i-L+1, 0), i

    # deque는 항상 오름차순 된 상태로 유지
    # 새로운 값은 마지막에 삽입
    # 새로운 값이 더 작거나 같을 경우 끝을 pop하고 새로운 값 삽입, 차피 필요한 값은 최솟값, 2번째로 작은 값이다.
    # deque에는 가장 작은 값, 2번째로 작은 값 2개만 관리
    while deq and deq[-1][1] >= A[i]:
        deq.pop()

    deq.append([i, A[i]])

    if not (start <= deq[0][0] <= i):
        deq.popleft()
    answer.append(deq[0][1])
print(*answer)
