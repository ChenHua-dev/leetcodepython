import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_rate = max(piles)
        lo, hi = 1, max(piles)
        while lo <= hi:
            rate = lo + (hi - lo) // 2
            hours = 0
            for p in piles:
                    hours += math.ceil(p / rate)

            if hours <= h:
                min_rate = min(min_rate, rate)
                hi = rate - 1
            else:
                lo = rate + 1
        return min_rate


if __name__ == '__main__':
    s = Solution()
    print(s.minEatingSpeed([3,6,7,11], 8))  # expect 4
    print(s.minEatingSpeed([30,11,23,4,20], 5))  # expect 30
    print(s.minEatingSpeed([30,11,23,4,20], 6))  # expect 23
