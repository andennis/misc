from typing import List
from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0
        if not bank:
            return -1
        queue = deque([(startGene, 0)])
        seen = set(startGene)
        bank_s = set(bank)
        while queue:
            gene, steps = queue.popleft()
            for i in range(len(gene)):
                for ch in ['A', 'C', 'G', 'T']:
                    if ch == gene[i]:
                        continue
                    next_gene = gene[:i] + ch + gene[i + 1:]
                    if next_gene not in seen and next_gene in bank_s:
                        if next_gene == endGene:
                            return steps + 1
                        seen.add(next_gene)
                        queue.append((next_gene, steps + 1))
        return -1


sln = Solution()
bank = ["AAAAAAAA","AAAAAAAC","AAAAAACC","AAAAACCC","AAAACCCC","AACACCCC","ACCACCCC","ACCCCCCC","CCCCCCCA"]
ans = sln.minMutation("AAAAAAAA", "CCCCCCCC", bank)
print(ans)
