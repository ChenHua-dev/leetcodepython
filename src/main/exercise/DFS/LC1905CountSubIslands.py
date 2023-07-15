from typing import List


class Solution:
    def __init__(self) -> None:
        self.same = False

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS = len(grid1); COLS = len(grid1[0])
        seen = set()
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] and (r, c) not in seen:
                    self.same = grid2[r][c] == grid1[r][c]
                    self.dfs(grid1, grid2, r, c, seen)
                    if self.same:
                        count += 1
        return count

    def dfs(self, grid1, grid2, r, c, seen) -> None:
        if 0 <= r < len(grid2) and 0 <= c < len(grid2[0]) and (r, c) not in seen and grid2[r][c] == 1:
            seen.add((r, c))
            if grid1[r][c] != grid2[r][c]:
                self.same = False
            self.dfs(grid1, grid2, r + 1, c, seen)
            self.dfs(grid1, grid2, r - 1, c, seen)
            self.dfs(grid1, grid2, r, c + 1, seen)
            self.dfs(grid1, grid2, r, c - 1, seen)


