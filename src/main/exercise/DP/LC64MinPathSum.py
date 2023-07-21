from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # https://leetcode.com/problems/minimum-path-sum/solutions/3345656/python-java-c-simple-solution-easy-to-understand/
        memo = []
        for _ in range(m):
            memo.append([0]*n)

        memo[0][0] = grid[0][0]
        for i in range(1, m):
            memo[i][0] = memo[i-1][0] + grid[i][0]
        for j in range(1, n):
            memo[0][j] = memo[0][j-1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = grid[i][j] + min(memo[i-1][j], memo[i][j-1])

        return memo[m-1][n-1]
