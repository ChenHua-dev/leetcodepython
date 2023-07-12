from typing import List, Set, Tuple


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        ROWS = len(board)
        COLS = len(board[0])
        i = 0
        for r in range(ROWS):
            for c in range(COLS):
                if self.dfs(board, word, visited, r, c, i):
                    return True
        return False

    def dfs(self, board: List[List[str]], word: str, visited: Set[Tuple[int]], r: int, c: int, i: int) -> bool:
        if i == len(word):
            return True
        if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == word[i] and (r, c) not in visited:
            visited.add((r, c))
            if self.dfs(board, word, visited, r + 1, c, i + 1):
                return True
            if self.dfs(board, word, visited, r - 1, c, i + 1):
                return True
            if self.dfs(board, word, visited, r, c + 1, i + 1):
                return True
            if self.dfs(board, word, visited, r, c - 1, i + 1):
                return True
            visited.remove((r, c))  # backtrack here
        return False


