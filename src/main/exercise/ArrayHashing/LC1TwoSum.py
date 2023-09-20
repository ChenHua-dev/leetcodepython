from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            compl = target - nums[i]
            if compl not in d:
                d[nums[i]] = i
            else:
                return [i, d[compl]]
        return [-1, -1]
