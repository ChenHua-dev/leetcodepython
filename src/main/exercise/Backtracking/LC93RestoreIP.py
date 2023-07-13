from typing import List

# https://www.youtube.com/watch?v=YqQvmemMbe4
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.dfs(s, res, "", 3, 0)
        return res

    def dfs(self, s: str, res: List[str], cur: str, dots: int, index: int) -> None:
        if dots == 0:
            if self.valid(s[index:]):
                cur += ("." + s[index:])
                res.append(cur)
            return

        for i in range(index, len(s)):
            if self.valid(s[index : i + 1]):
                length = len(cur)
                if dots == 3:
                    cur += s[index : i + 1]
                else:
                    cur += ("." + s[index : i + 1])
                self.dfs(s, res, cur, dots - 1, i + 1)
                cur = cur[:length]  # backtrack, remove last element

    def valid(self, s) -> bool:
        if len(s) > 3:
            return False
        if len(s) < 1:
            return False
        if s[0] == "0" and len(s) > 1:
            return False
        if int(s) > 255:
            return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.restoreIpAddresses("25525511135"))
