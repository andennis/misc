from typing import List
from collections import deque


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        dq = deque([(start, 0)])

        while dq:
            st0, cnt = dq.popleft()
            if st0 == end:
                return cnt

            for i, ch0 in enumerate(st0):
                for ch1 in "ACGT":
                    if ch0 != ch1 and (st1 := st0[:i] + ch1 + st0[i + 1:]) in bank:
                        bank.remove(st1)
                        dq.append((st1, cnt + 1))

        return -1

sln = Solution()
bank = ["AAAAAAAA","AAAAAAAC","AAAAAACC","AAAAACCC","AAAACCCC","AACACCCC","ACCACCCC","ACCCCCCC","CCCCCCCA"]
ans = sln.minMutation("AAAAAAAA", "CCCCCCCC", bank)
print(ans)
