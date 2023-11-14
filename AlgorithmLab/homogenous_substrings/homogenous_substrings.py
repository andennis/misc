# https://leetcode.com/problems/count-number-of-homogenous-substrings/?envType=daily-question&envId=2023-11-09
# ---
# Given a string s, return the number of homogenous substrings of s.
# Since the answer may be too large, return it modulo 10^9 + 7.
#
# A string is homogenous if all the characters of the string are the same.
# A substring is a contiguous sequence of characters within a string.
#
# Example 1:
# Input: s = "abbcccaa"
# Output: 13
# Explanation: The homogenous substrings are listed as below:
# "a" appears 3 times.
# "aa" appears 1 time.
# "b" appears 2 times.
# "bb" appears 1 time.
# "c" appears 3 times.
# "cc" appears 2 times.
# "ccc" appears 1 time.
# 3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.

MOD_VAL = 1000000007


def count_homogenous(s: str) -> int:
    result = 0
    i = 0
    while i < len(s):
        from_i, to_i = _find_homogenous_series(s, i)
        result += _count_homogenous_in_series(s[from_i:to_i])
        i = to_i

    return result % MOD_VAL


def _find_homogenous_series(s: str, from_ind: int) -> tuple[int, int]:
    ch = s[from_ind]
    to_ind = len(s)
    for i in range(from_ind+1, len(s)):
        if ch != s[i]:
            to_ind = i
            break
    return from_ind, to_ind


def _count_homogenous_in_series(s: str) -> int:
    result = 0
    s_len = len(s)
    for i in range(s_len):
        s_size = i + 1
        result += s_len - s_size + 1
    return result
