import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):

    input_parenthesis = sys.stdin.readline().rstrip()
    stack = deque()
    fail = False
    for character in input_parenthesis:
        if character == '(':
            stack.append(character)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                fail = True
                break

    if fail or stack:
        print('NO')
    else:
        print('YES')
