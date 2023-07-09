from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        index = 0
        self.dfs(s, res, part, index)
        return res

    def dfs(self, s: str, res: List[List[str]], part: List[str], i: int) -> None:
        if i == len(s):
            res.append(part.copy())
            return
        for j in range(i, len(s)):
            if self.is_palindrome(s, i, j):
                part.append(s[i:j+1])
                self.dfs(s, res, part, j + 1)
                part.pop()

    def is_palindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.partition("aab"))
    print(s.partition("a"))
