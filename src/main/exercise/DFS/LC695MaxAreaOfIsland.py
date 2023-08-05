from typing import List, Set, Tuple

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROWS = len(grid)
        COLS = len(grid[0])
        max_area = 0
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                max_area = max(max_area, self.dfs(grid, r, c, visited))
        return max_area

    def dfs(self, grid: List[List[int]], r: int, c: int, visited: Set[Tuple[int, int]]) -> int:
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0 or (r,c) in visited:
            return 0

        visited.add((r, c))
        local_max = 1
        local_max += self.dfs(grid, r+1, c, visited)
        local_max += self.dfs(grid, r-1, c, visited)
        local_max += self.dfs(grid, r, c-1, visited)
        local_max += self.dfs(grid, r, c+1, visited)
        return local_max
