from typing import List


def find_max_length_v1(nums: List[int]) -> int:
    d = {0: 0}
    max_ln = 0
    sm = 0
    for i in range(1, len(nums) + 1):
        sm += nums[i-1]
        v = i - 2 * sm
        if v in d:
            ln = i - d[v]
            if ln > max_ln:
                max_ln = ln
        else:
            d[i - 2 * sm] = i

    return max_ln


def find_max_length_v2(nums: List[int]) -> int:
    max_ln = 0
    n = len(nums)
    arr = [-2] * (n * 2 + 1)
    arr[n] = -1
    count = 0
    for i in range(n):
        count += 1 if nums[i] == 1 else -1
        if arr[count + n] >= -1:
            max_ln = max(max_ln, i - arr[count + n])
        else:
            arr[count + n] = i

    return max_ln
