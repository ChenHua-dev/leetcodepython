from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        total = 0
        candidates.sort()
        self.dfs(candidates, target, res, sub, 0, total)
        return res

    def dfs(self, candidates: List[int], target: int, res: List[List[int]], sub: List[int], pos: int, total:int) -> None:
        if total == target:
            res.append(sub.copy())
            return
        if total > target:
            return

        prev = -float('inf')
        for i in range(pos, len(candidates)):
            if candidates[i] == prev:
                continue
            sub.append(candidates[i])
            self.dfs(candidates, target, res, sub, i + 1, total + candidates[i])
            sub.pop()
            prev = candidates[i]


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))  # [[1,1,6],[1,2,5],[1,7],[2,6]]
    print(s.combinationSum2([2,5,2,1,2], 5))  # [[1,2,2],[5]]
    print(s.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 27))  # []
    print(s.combinationSum2([1,2], 4))  # []
