A = int(input())
B = int(input())
C = int(input())

total = str(A * B * C)

numbers = [0 for _ in range(10)]

for char in total:
    numbers[int(char)] += 1

print(*numbers, end='\n')

