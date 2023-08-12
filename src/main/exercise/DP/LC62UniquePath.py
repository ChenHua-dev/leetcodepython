class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n
        dp = []
        for i in range(rows):
            tmp = []
            for j in range(cols):
                tmp.append(1)
            dp.append(tmp)

        for i in range(rows-2, -1, -1):
            for j in range(cols-2, -1, -1):
                dp[i][j] = dp[i][j+1] + dp[i+1][j]
        return dp[0][0]
    
