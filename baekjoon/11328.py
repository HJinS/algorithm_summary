import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    word1, word2 = map(str, sys.stdin.readline().rstrip().split(' '))
    word_map1, word_map2 = {}, {}

    for char in word1:
        word_map1[char] = 1 if char not in word_map1 else word_map1[char] + 1

    for char in word2:
        word_map2[char] = 1 if char not in word_map2 else word_map2[char] + 1

    keys1, keys2 = word_map1.keys(), word_map2.keys()

    target_keys = keys1 | keys2
    result = "Possible"
    for key in target_keys:
        item1, item2 = 0, 0
        if key in word_map1:
            item1 = word_map1[key]
        if key in word_map2:
            item2 = word_map2[key]
        if abs(item1 - item2) != 0:
            result = "Impossible"
    print(result)