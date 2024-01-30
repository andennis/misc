from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[-1] = questions[-1][0]

        for i in range(n - 2, -1, -1):
            dp[i] = questions[i][0]
            skip = questions[i][1]
            if i + skip + 1 < n:
                dp[i] += dp[i + skip + 1]

            dp[i] = max(dp[i], dp[i + 1])

        return dp[0]

    def mostPoints_v2(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[-1] = questions[-1][0]
        for i in range(n - 2, -1, -1):
            points, skip = questions[i]
            p1 = points + (dp[i + skip + 1] if i + skip + 1 < n else 0)
            p2 = dp[i + 1]
            dp[i] = max(p1, p2)

        return dp[0]



sln = Solution()
print(sln.mostPoints_v2([[12,46],[78,19],[63,15],[79,62],[13,10]]))