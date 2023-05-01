import sys
from collections import deque


bracket_mapping = {
    ')': '(',
    ']': '['
}

while True:
    input_string = sys.stdin.readline().rstrip()

    if input_string == '.':
        break

    stack = deque()
    fail = False
    for character in input_string:
        if character in set(list(bracket_mapping.values())):
            stack.append(character)
        elif character in set(list(bracket_mapping.keys())):
            if not stack or stack[-1] != bracket_mapping[character]:
                print('no')
                fail = True
                break
            else:
                stack.pop()

    if fail:
        continue

    if stack:
        print('no')
    else:
        print('yes')
