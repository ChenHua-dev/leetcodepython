from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        index = 0
        self.dfs(nums, res, subset, index)
        return res

    def dfs(self, nums: List[int], res: List[int], subset: List[int], i) -> None:
        if i == len(nums):
            res.append(subset.copy())
            return

        for num in nums:
            if num not in subset:
                subset.append(num)
                self.dfs(nums, res, subset, i + 1)
                subset.pop()

    # def dfs(self, nums: List[int], res: List[int], subset: List[int], i) -> None:
    #     if len(subset) == len(nums):
    #         res.append(subset.copy())
    #         return
    #
    #     for i in range(len(nums)):
    #         curr = nums[i]
    #         if curr not in subset:
    #             subset.append(curr)
    #             self.dfs(nums, res, subset, i + 1)
    #             subset.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.permute([3,7,0]))
