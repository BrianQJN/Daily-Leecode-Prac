"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
substrings
 respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # if sum of len s1 and s2 is not equal to s3 len, return false
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        
        # initialize the dp array
        # dp[i][j] records whether s1[0:i] and s2[0:j] can form s3[0:i+j] interleavly
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):
                # if cur char in s1 is equal to cur char in s3
                if i > 0 and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i-1][j]
                # if cur char in s2 is equal to cur char in s3
                if j > 0 and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j-1] or dp[i][j]
                
                print(i, j)
                print(dp[i][j])

        return dp[m][n]
    
Solution.isInterleave(Solution, "abc", "def", "adbcef")
