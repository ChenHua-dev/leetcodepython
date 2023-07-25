class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ""
        dp = []
        for i in range(len(s)):
            dp.append([False]*len(s))
        for i in range(len(s)):
            dp[i][i] = True
            palindrome = s[i]

        for i in range(len(s)):
            for j in range(i):
                if s[j] == s[i] and (j+1 == i or dp[j+1][i-1]):
                    dp[j][i] = True
                    if(i-j+1) > len(palindrome):
                        palindrome = s[j:i+1]
        return palindrome
    
