import sys

input_str = sys.stdin.readline().rstrip()

alphabet_count_list = [0 for i in range(26)]

for character in input_str:
    idx = ord(character) - ord('a')
    alphabet_count_list[idx] += 1

print(*alphabet_count_list)