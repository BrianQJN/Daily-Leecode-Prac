"""
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

Example:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rab b bit
rabb b it
rab b bit
"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        # initialize the dynamic array dp
        # dp[i][j] represents the number of distinct subsequences of the first i chars in s which equals first j chars in t
        dp = [[0] * (n+1) for _ in range(m+1)]

        # set the default value for dp array
        # since for the empty string t, there is only one way to choose, i.e. choose empty string in s too
        for i in range(m + 1):
            dp[i][0] = 1
        
        # traverse the dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[m][n]