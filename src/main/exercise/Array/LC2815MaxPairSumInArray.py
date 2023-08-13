from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res = -1
        for i in range(len(nums)):
            fix_i = nums[i]
            for j in range(i+1, len(nums)):
                fix_j = nums[j]
                if self.max_digit(fix_i) == self.max_digit(fix_j):
                    res = max(res, fix_i + fix_j)
        return res

    def max_digit(self, num: int):
        lst = []
        while num != 0:
            lst.append(num % 10)
            num = num // 10
        return max(lst)
