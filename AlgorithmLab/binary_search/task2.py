from typing import List
# from math import inf


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def check(target: int):
            sm = 0
            i = 0
            for s in sweetness:
                sm += s
                if sm >= target:
                    i += 1
                    if i == k + 1:
                        return True
                    sm = 0
            return False

        left = min(sweetness)
        right = sum(sweetness) // (k + 1)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right


sln = Solution()
print(sln.maximizeSweetness([1,2,3,4,5,6,7,8,9], 5))  # 6
print(sln.maximizeSweetness([1,2,2,1,2,2,1,2,2], 2))  # 5
print(sln.maximizeSweetness([5,6,7,8,9,1,2,3,4], 8))  # 1
print(sln.maximizeSweetness([90670,55382,95298,95795,73204,41464,18675,30104,47442,55307], 6))  # 55382

# data = [19679,20653,68010,3714,54485,548,41366,11201,47138,70768,1050,87246,17114,56157,13235,65363,30444,56929,21969,22308]
# print(sln.maximizeSweetness(data, 0))

# data = [87002,22650,61737,4432,87341,67643,13454,83823,87836,2978,99313,82797,77350,55994,31403,73836,54451,54807,60146,
#         72381,7271,37633,32603,33752,78004,76288,94608,3516,98287,16577,36186,40401,70733,35764,76303,74279,18351,74113,
#         26480,64253,49402,47512,37185,42488,43068,3542,55773,91365,86770,52915]
# print(sln.maximizeSweetness(data, 3))  # 641293
