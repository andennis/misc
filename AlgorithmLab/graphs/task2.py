from typing import List
from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        MAX_STEP_SIZE = 6
        n = len(board)
        finish = n * n - 1
        queue = deque([(0, 0)])
        seen = {0}
        while queue:
            pos, steps = queue.popleft()
            for next_pos in range(pos + 1, min(pos + MAX_STEP_SIZE, finish) + 1):
                r, c = divmod(next_pos, n)
                y = n - 1 - r
                x = (n - 1 - c) if r % 2 else c
                if board[y][x] != -1:
                    next_pos = board[y][x] - 1

                if next_pos not in seen:
                    if next_pos == finish:
                        return steps + 1

                    queue.append((next_pos, steps + 1))
                    seen.add(next_pos)

        return -1


data = [
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,35,-1,-1,13,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,15,-1,-1,-1,-1]
]

# data = [
#     [-1,-1,19,10,-1],
#     [ 2,-1,-1, 6,-1],
#     [-1,17,-1,19,-1],
#     [25,-1,20,-1,-1],
#     [-1,-1,-1,-1,15]
# ]
sln = Solution()
print(sln.snakesAndLadders(data))