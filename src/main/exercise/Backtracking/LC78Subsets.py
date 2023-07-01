from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        self.dfs(nums, res, subset, 0)
        return res

    def dfs(self, nums: List[int], res: List[int], subset: List[int], index) -> None:
        if index == len(nums):
            res.append(subset.copy())
            return
        curr = nums[index]
        subset.append(curr)
        self.dfs(nums, res, subset, index + 1)
        subset.pop()
        self.dfs(nums, res, subset, index + 1)


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1,2,3]))

