from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        v_pac = set()
        v_atl = set()

        for c in range(COLS):
            self.dfs(heights, v_pac, 0, c, heights[0][c])
            self.dfs(heights, v_atl, ROWS - 1, c, heights[ROWS-1][c])

        for r in range(ROWS):
            self.dfs(heights, v_pac, r, 0, heights[r][0])
            self.dfs(heights, v_atl, r, COLS-1, heights[r][COLS-1])

        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in v_pac and (i,j) in v_atl:
                    res.append([i,j])
        return res

    def dfs(self, heights, visited, i, j, curr_height) -> None:
        ROWS = len(heights)
        COLS = len(heights[0])
        if i < 0 or i >= ROWS or j < 0 or j >= COLS or (i,j) in visited or curr_height > heights[i][j]:
            return
        visited.add((i, j))
        self.dfs(heights, visited, i + 1, j, heights[i][j])
        self.dfs(heights, visited, i - 1, j, heights[i][j])
        self.dfs(heights, visited, i, j + 1, heights[i][j])
        self.dfs(heights, visited, i, j - 1, heights[i][j])
