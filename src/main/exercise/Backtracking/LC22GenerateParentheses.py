from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = ""
        left_count = 0
        right_count = 0
        self.dfs(n, res, cur, left_count, right_count)
        return res

    def dfs(self, n: int, res: List[str], cur: str, left_count: int, right_count: int) -> None:
        if len(cur) == n*2:
            res.append(cur)

        if left_count < n:
            cur += "("
            self.dfs(n, res, cur, left_count + 1, right_count)
            cur = cur[:-1]
        if right_count < left_count:
            cur += ")"
            self.dfs(n, res, cur, left_count, right_count + 1)
            cur = cur[:-1]


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))  # ["((()))","(()())","(())()","()(())","()()()"]
    print(s.generateParenthesis(1))  # ["()"]
