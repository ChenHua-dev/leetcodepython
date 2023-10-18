from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left = 1
        prefix = [1] * n
        for i in range(1, n):
            left = left * nums[i-1]
            prefix[i] = left

        right = 1
        suffix = [1] * n
        for i in range(n-2, -1, -1):
            right = right * nums[i+1]
            suffix[i] = right

        res = [0] * n
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([2,3,4,5]))
