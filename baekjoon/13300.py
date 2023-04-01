import sys

N, K = map(int, sys.stdin.readline().strip().split(' '))


count_arr = [0 for i in range(13)]

for i in range(N):
    gender, level = map(int, sys.stdin.readline().rstrip().split(' '))

    count_arr[level + 6 * gender] += 1

result = 0
for count in count_arr[1:]:
    if count % K == 0:
        result += count // K
    else:
        result += (count // K) + 1

print(result)
