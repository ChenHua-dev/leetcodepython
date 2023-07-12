from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    count += 1
                    self.dfs(grid, r, c, visited)
        return count

    def dfs(self, grid, r, c, visited) -> None:
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or (r,c) in visited:
            return

        if grid[r][c] == '1':
            visited.add((r,c))
            self.dfs(grid, r + 1, c, visited)
            self.dfs(grid, r - 1, c, visited)
            self.dfs(grid, r, c - 1, visited)
            self.dfs(grid, r, c + 1, visited)
