from collections import deque

"""
스텍에 수를 쌓으면서 현재 idx의 숫자를 기준으로 앞의 숫자들의 뒤큰수를 구하는 형식
"""
def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    stack = deque()

    for idx, num in enumerate(numbers):
        if idx == 0:
            stack.append(idx)
            continue
        while stack and numbers[stack[-1]] < num:
            answer_idx = stack.pop()
            answer[answer_idx] = num
        stack.append(idx)
    return answer
