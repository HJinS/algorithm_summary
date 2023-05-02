import sys
from collections import deque

bracket = sys.stdin.readline().rstrip()

bracket_stack = deque()

SUM = 0
NUM = 1

"""
boj 10799 쇠 막대기 문제의 아이디어와 비슷하게 붙어있는 () 혹은 []를 만나면
sum에 점수를 더해줌. () 혹은 []이 몇 점인가는 중첩된 소괄호/대괄호의 곱으로
계산 가능하고 이는 변수 num에 저장이 됨. 

(()[[]])([])

2*(2+3*(3)) + 2*(3) -> 2*2 + 2*3*3 + 2*3 의 형태로 풀어서 계산
pop을 할 때마다 나누어 주어서 다은 계산에 쓰이도록
"""

for idx, character in enumerate(bracket):
    # print(f' stack = {bracket_stack}, SUM = {SUM}, NUM = {NUM}')
    if character == '(':
        NUM *= 2
        bracket_stack.append(character)
    elif character == '[':
        NUM *= 3
        bracket_stack.append(character)
    elif character == ')':
        if not bracket_stack or bracket_stack[-1] != '(':
            print(0)
            exit()
        if bracket[idx-1] == '(':
            SUM += NUM
        bracket_stack.pop()
        NUM //= 2
    elif character == ']':
        if not bracket_stack or bracket_stack[-1] != '[':
            print(0)
            exit()
        if bracket[idx-1] == '[':
            SUM += NUM
        bracket_stack.pop()
        NUM //= 3
if bracket_stack:
    print(0)
else:
    print(SUM)
