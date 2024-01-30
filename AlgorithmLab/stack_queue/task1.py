from typing import List


class Solution:

    def longest_subarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        min_i = 0
        max_i = 0
        max_ln = 1
        l = 0
        for r in range(1, len(nums)):
            if nums[r] <= nums[min_i]:
                min_i = r
            if nums[r] >= nums[max_i]:
                max_i = r

            while abs(nums[max_i] - nums[min_i]) > limit:
                l = (min_i if min_i <= max_i else max_i) + 1

                if l > min_i:
                    min_i = l
                    for i in range(l + 1, r):
                        if nums[i] <= nums[min_i]:
                            min_i = i
                if l > max_i:
                    max_i = l
                    for i in range(l + 1, r):
                        if nums[i] >= nums[max_i]:
                            max_i = i

            max_ln = max(max_ln, r - l + 1)

        return max_ln


r = Solution()

l1 = [34,24,70,27,40,26,32,47,11,36,12,97,58,12,84,74,83,44,30,50,40,6,42,24,41,75,39,32,43,13,70,79,75,77,12,32,29,3,32,
     52,10,35,71,10,94,10,3,82,2,38,97,46,64,61,20,13,65,100,42,10,66,86,23,23,100,20,19,41,40,14,91,66,78,38,17,27,19,
     70,93,5,100,41,80,87,71,96,89,27,23,39,56,69]

result = r.longest_subarray(l1, 72)
print(result)
