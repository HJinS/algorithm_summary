import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

arr = [0] * N

stack = deque()
current = 1
answer = ""
for _ in range(N-1, -1, -1):
    num = int(sys.stdin.readline().rstrip())

    while current <= num:
        stack.append(current)
        answer += "+\n"
        current += 1
    if stack[-1] != num:
        print('NO')
        exit()
    stack.pop()
    answer += "-\n"

print(answer)


##################################################

import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
stack2 = deque()
arr = [0] * N
answer = ""
for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    arr[i] = num
checked_idx = 0
for i in range(1, N+1):
    stack2.append(i)
    answer += "+\n"

    while stack2 and arr[checked_idx] == stack2[-1]:
        stack2.pop()
        answer += "-\n"
        checked_idx += 1

if stack2:
    print("NO")
else:
    print(answer)