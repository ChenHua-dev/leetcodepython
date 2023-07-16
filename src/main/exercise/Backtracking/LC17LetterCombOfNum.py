from typing import List


class Solution:
    def __init__(self) -> None:
        self.map = {"2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz"}

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits) <= 0:
            return res
        index = 0
        substr = "" # start of the substring is ""
        self.dfs(digits, res, index, substr)
        return res

    def dfs(self, digits: str, res: List[str], index: int, substr: str) -> None:
        if index >= len(digits):
            res.append(substr)
            return

        curr_char = self.map[digits[index]]
        for c in curr_char:
            substr += c
            self.dfs(digits, res, index + 1, substr)
            substr = substr[:-1]


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(s.letterCombinations(""))  # []
    print(s.letterCombinations("2"))  # ["a","b","c"]
