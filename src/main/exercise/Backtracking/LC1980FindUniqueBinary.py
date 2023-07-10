from typing import List, Set


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        binary_set = {n for n in nums}
        curr = ""
        res = self.dfs(nums, binary_set, curr)
        return res

    def dfs(self, nums: List[str], binary_set: Set[str], curr: str) -> str:
        if len(curr) == len(nums):
            if curr in binary_set:
                return None
            else:
                return curr

        res = self.dfs(nums, binary_set, curr + "0")
        if res:
            return res
        res = self.dfs(nums, binary_set, curr + "1")
        if res:
            return res


if __name__ == '__main__':
    s = Solution()
    print(s.findDifferentBinaryString(["01","10"]))
    print(s.findDifferentBinaryString(["00","01"]))
    print(s.findDifferentBinaryString(["111","011","001"]))
