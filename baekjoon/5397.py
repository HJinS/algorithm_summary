import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())


for _ in range(N):
    original_input = sys.stdin.readline().rstrip()

    left = deque()
    right = deque()

    for char in original_input:
        if char == '<':
            if left:
                right.append(left.pop())
        elif char == '>':
            if right:
                left.append(right.pop())
        elif char == '-':
            if left:
                left.pop()
        else:
            left.append(char)
    result = []
    if left:
        result.extend(list(left))
    if right:
        result.extend(reversed(list(right)))
    print(''.join(result))
