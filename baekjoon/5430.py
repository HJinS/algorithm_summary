import sys
from collections import deque

total_test_case_num = int(sys.stdin.readline().rstrip())


def safe_int(value, default=None):
    try:
        return int(value)
    except:
        return default


for _ in range(total_test_case_num):
    instruction_list = list(sys.stdin.readline().rstrip())
    list_len = int(sys.stdin.readline().rstrip())
    initial_deque = deque(map(safe_int, sys.stdin.readline().rstrip()[1:-1].split(',')))

    is_reversed = False
    fail = False
    if list_len == 0:
        initial_deque = deque()
    for instruction in instruction_list:
        if instruction == 'R':
            is_reversed = not is_reversed
        elif instruction == 'D':
            if not initial_deque:
                print('error')
                fail = True
                break
            if is_reversed:
                initial_deque.pop()
            else:
                initial_deque.popleft()

    if not fail:
        if not initial_deque:
            print('[]')
        elif is_reversed:
            print('[', end='')
            for idx in range(len(initial_deque)-1, 0, -1):
                print(initial_deque[idx], end=',')
            print(initial_deque[0], end=']\n')
        else:
            print('[', end='')
            for idx in range(len(initial_deque)-1):
                print(initial_deque[idx], end=',')
            print(initial_deque[-1], end=']\n')
