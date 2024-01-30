from typing import List
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def lengthOfLIS_v2(self, nums: List[int]) -> int:
        lst = []
        for num in nums:
            i = bisect_left(lst, num)

            if i == len(lst):
                lst.append(num)

            else:
                lst[i] = num

        return len(lst)

    def lengthOfLIS_v3(self, nums: List[int]) -> int:
        sub = [nums[0]]

        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                i = 0
                while num > sub[i]:
                    i += 1
                sub[i] = num

        return len(sub)

sln = Solution()
print(sln.lengthOfLIS_v3([10,9,2,5,3,7,101,18,1]))
