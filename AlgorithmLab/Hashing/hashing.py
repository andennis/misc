from typing import List


def find_max_length(nums: List[int]) -> int:
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
