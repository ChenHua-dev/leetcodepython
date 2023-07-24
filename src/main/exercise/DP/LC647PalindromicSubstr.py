class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        memo = []
        for _ in range(len(s)):
            temp = []
            for _ in range(len(s)):
                temp.append(False)
            memo.append(temp)

        for i in range(len(s)):
            for j in range(i):
                if i - j <= 2:
                    memo[j][i] = (s[j] == s[i])
                else:
                    memo[j][i] = (s[j] == s[i] and memo[j + 1][i - 1])
                if memo[j][i]:
                    count += 1
            memo[i][i] = True
            count += 1

        return count
