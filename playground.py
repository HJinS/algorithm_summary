from typing import List


def test1(N: int) -> int:
    """
    각각의 배수가 마지막으로 끝나는 위치 확인 -> 3 * k <= N -> K <= N / 3 -> K == N // 3
    """

    end_3 = N // 3
    end_5 = N // 5
    end_15 = N // 15

    sum_3 = end_3*(3 + 3 + (end_3 - 1)*3) / 2
    sum_5 = end_5*(5 + 5 + (end_5 - 1)*5) / 2
    sum_15 = end_15*(15 + 15 + (end_15 - 1)*15) / 2
    return int(sum_3 + sum_5 - sum_15)



def test2(arr: List) -> bool:
    check_set = set()
    n = len(arr)

    for i in range(n):
        check_target = 100 - arr[i]
        if check_target not in check_set:
            check_set.add(arr[i])
        else:
            return True
    return False


print(test2([4, 13, 63, 87]))