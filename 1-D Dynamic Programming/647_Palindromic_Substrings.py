"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
"""
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        # initialize the dp[i][j] to store the substring status
        dp = [[False] * n for _ in range(n)]
        count = 0
        
        # initialize the diagonal elements of the dp[i][j] to True
        # since that the single character must be palindromic
        for i in range(n):
            dp[i][i] = True
            count += 1

        # start from the substrings with length 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                count += 1

        # calculate the substrings with length greater than 2
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                # for a string if the head == tail and the substring between them are palindromic
                # the string must be palindromic
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    count += 1

        return count