from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        if n < 2:
            return nums[0]

        numsExcludeLast = nums[:n - 1]
        numsExcludeFirst = nums[1:]

        excludeLastAns = self.dp_helper(numsExcludeLast)
        excludeFirstAns = self.dp_helper(numsExcludeFirst)

        return max(excludeLastAns, excludeFirstAns)

    def dp_helper(self, nums: List[int]):
        n = len(nums)
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return max(dp)
