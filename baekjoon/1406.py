# two stack solution
from sys import stdin, stdout
left = list(stdin.readline())
left.pop()
stdin.readline()
right = []
for oper in stdin.read().splitlines():
    if oper == "L":
        if left:
            right.append(left.pop())
    elif oper == "D":
        if right:
            left.append(right.pop())
    elif oper == "B":
        if left:
            left.pop()
    else:
        left.append(oper[-1])
stdout.write("".join(left))
stdout.write("".join(reversed(right)))