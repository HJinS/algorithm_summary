import sys
from collections import deque

bracket = list(sys.stdin.readline().rstrip())

stack = deque()

bracket_mapping = {
    '(': ')'
}
open_set = set(bracket_mapping.keys())
close_set = set(bracket_mapping.values())

is_open_added = False

answer = 0
for item in bracket:
    if item in open_set:
        stack.append(item)
        is_open_added = True
    else:
        stack.pop()
        if is_open_added:
            answer += len(stack)
        else:
            answer += 1
        is_open_added = False

print(answer)
