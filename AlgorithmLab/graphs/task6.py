from typing import List
from collections import defaultdict


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def is_in_circle(cx: int, cy: int, cr: int, check_point: tuple[int, int]) -> bool:
            return ((check_point[0] - cx) ** 2 + (check_point[1] - cy) ** 2) <= cr ** 2

        def detonated_num(bomb: int) -> int:
            count = 1
            for next_bomb in graph[bomb]:
                if next_bomb not in seen:
                    seen.add(next_bomb)
                    count += detonated_num(next_bomb)
            return count

        graph = defaultdict(list)
        for i, b1 in enumerate(bombs):
            for j, b2 in enumerate(bombs):
                if i == j:
                    continue
                if is_in_circle(b1[0], b1[1], b1[2], (b2[0], b2[1])):
                    graph[i].append(j)

        max_b = 0
        for i in range(len(bombs)):
            seen = {i}
            max_b = max(max_b, detonated_num(i))

        return max_b


data = [[4,4,3],[4,4,3]]
sln = Solution()
print(sln.maximumDetonation(data))