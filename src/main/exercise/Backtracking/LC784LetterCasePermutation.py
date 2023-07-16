from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        cur = ""
        index = 0
        self.dfs(s, res, cur, index)
        return res

    def dfs(self, s: str, res: List[str], cur: str, index: int) -> None:
        if index == len(s):
            res.append(cur)
            return

        letter = s[index]
        if letter.isnumeric():
            cur += letter
            self.dfs(s, res, cur, index + 1)
            cur = cur[:-1]

        if letter.isalpha():
            cur += letter.lower()
            self.dfs(s, res, cur, index + 1)
            cur = cur[:-1]

            cur += letter.upper()
            self.dfs(s, res, cur, index + 1)
            cur = cur[:-1]

