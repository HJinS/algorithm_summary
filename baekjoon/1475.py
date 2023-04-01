num = input()

numbers = [0 for i in range(10)]

for char in num:
    numbers[int(char)] += 1

numbers[6] += numbers[9]

numbers[9] = 0

max_num = -1
for idx, number in enumerate(numbers):
    if max_num < number and idx != 6:
        max_num = number
    elif max_num < number and idx == 6:
        max_num = number // 2 + 1 if number % 2 != 0 else number // 2

print(max_num)



