A = input()
B = input()

A_work_map = {}
B_work_map = {}

for char in A:
    if char not in A_work_map:
        A_work_map[char] = 1
    else:
        A_work_map[char] += 1

for char in B:
    if char not in B_work_map:
        B_work_map[char] = 1
    else:
        B_work_map[char] += 1

key_set_a = set(A_work_map.keys())
key_set_b = set(B_work_map.keys())

keys = key_set_a | key_set_b
cnt = 0

for char in keys:
    A_item, B_item = 0, 0
    if char in A_work_map:
        A_item = A_work_map[char]
    if char in B_work_map:
        B_item = B_work_map[char]

    cnt += abs(A_item - B_item)
print(cnt)
