import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
count = 0
for _ in range(N):
    stack = deque()
    input_string = sys.stdin.readline().rstrip()

    for character in input_string:
        if stack and character == stack[-1]:
            stack.pop()
        else:
            stack.append(character)

    if not stack:
        count += 1
print(count)
