from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def check(prnts: str) -> bool:
            count = 0
            for ch in prnts:
                count += 1 if ch == "(" else -1
                if count < 0:
                    return False
            return count == 0

        def backtrack(prnts: str):
            if check(prnts):
                ans.append(prnts)
                return

            for i in range(n * 2):
                ch = "(" if prnts[i] == ")" else ")"
                next_prnts = prnts[:i] + ch + prnts[i+1:]
                if next_prnts not in seen:
                    seen.add(next_prnts)
                    backtrack(next_prnts)

        ans = []
        seen = set()
        backtrack("(" * n * 2)
        return ans


sln = Solution()
print(sln.generateParenthesis(2))
