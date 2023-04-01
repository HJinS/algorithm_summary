import sys
from collections import deque

count = int(sys.stdin.readline().rstrip())
stack = deque()
for i in range(count):
    instruction = sys.stdin.readline().rstrip().split(' ')
    if instruction[0] == 'push':
        stack.append(instruction[1])
    elif instruction[0] == 'top':
        if len(stack) == 0:
            print(-1)
            continue
        print(stack[-1])
    elif instruction[0] == 'pop':
        if len(stack) == 0:
            print(-1)
            continue
        print(stack.pop())
    elif instruction[0] == 'size':
        print(len(stack))
    elif instruction[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

