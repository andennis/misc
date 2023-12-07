from typing import List


def find_max_length(nums: List[int]) -> int:
    prefix = [0]
    for i in range(len(nums)):
        prefix.append(nums[i] + prefix[i])

    d = {0: 0}
    max_ln = 0
    for i in range(1, len(prefix)):
        v = i - 2 * prefix[i]
        if v in d:
            ln = i - d[v]
            if ln > max_ln:
                max_ln = ln
        else:
            d[i - 2 * prefix[i]] = i

    return max_ln
