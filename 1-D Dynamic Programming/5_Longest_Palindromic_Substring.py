"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)

        # initialize the dp to record the status of the substring
        dp = [[False] * n for _ in range(n)]
        start, max_len = 0, 1

        # initialize the diagonal elements in dp to True
        # because dp[i][j] is a char, always be the palindrome
        for i in range(n):
            dp[i][i] = True

        # then we start from the substring with length 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start, max_len = i, 2
        
        # caculate the substring with length greater than 2
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                # for a string if the head == tail and the substring between the head and the tail is palindromic
                # the string is palindromic too
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    start, max_len = i, length

        return s[start:start + max_len]