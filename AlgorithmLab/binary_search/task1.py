from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[i - 1])

        ans = []
        for q in queries:
            l = 0
            r = len(prefix) - 1
            while l <= r:
                mid = (l + r) // 2
                # if prefix[mid] == q:
                #     l = mid + 1
                #     break
                if prefix[mid] <= q:
                    l = mid + 1
                else:
                    r = mid - 1

            ans.append(l)

        return ans


sln = Solution()
print(sln.answerQueries([4,5,2,1], [3,10,21]))