from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0] * length

        tmp = 1
        prefix = [0] * length
        for i in range(length):
            prefix[i] = tmp
            tmp *= nums[i]

        tmp = 1
        postfix = [0] * length
        for i in range(length - 1, -1, -1):
            postfix[i] = tmp
            tmp *= nums[i]

        for i in range(length):
            res[i] = prefix[i] * postfix[i]

        return res
