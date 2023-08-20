"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # initialize the dynamic dp array
        # dp[i][j] represents the min operations needed to be done convert first i chars in word1 to first j chars in word2
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # set the default value in dp array
        # since if one of the word is empty, we can only remove the char in another word, so only i or j operation
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # traverse the dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # if the cur char is the same, we don't need extra operation
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                # if we insert: operation = dp[i][j-1] + 1，就是word1的前i个和word2的前j-1个匹配，所以要在word1插入一个，才能和前j个匹配
                # if we delete: operation = dp[i-1][j] + 1，就是i-1个已经和j个匹配了，所以word1里面需要删一个多余的
                # if we replace: operation = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1

        return dp[m][n]