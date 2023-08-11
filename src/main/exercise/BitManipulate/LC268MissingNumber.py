from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        missing = 0
        for i in range(1, n+1):
            missing ^= i

        for i in range(n):
            missing ^= nums[i]
        return missing
