from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        comb = []
        start_index = 1
        self.dfs(n, k, res, comb, start_index)
        return res

    def dfs(self, n: int, k: int, res: List[List[int]], comb: List[int], start_index: int) -> None:
        if len(comb) == k:
            res.append(comb.copy())
            return

        for i in range(start_index, n + 1):
            comb.append(i)
            self.dfs(n, k, res, comb, i + 1)
            comb.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
    print(s.combine(1, 1))
    print(s.combine(4, 3))
