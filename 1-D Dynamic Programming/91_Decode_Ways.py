"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        # dp[i] presents total number of ways to decode start from ith char in string s
        # set last element dp[n] to 1, means there is only one way to decode if the string is null string
        dp = [0] * (n + 1)
        dp[n] = 1

        for i in range(n-1, -1, -1):
            # if s[i] is '0', dp[i] is 0, because '0' can decode alone
            if s[i] == '0':
                dp[i] = 0
            else:
            # if s[i] is '1', there are two ways to decode, one is decode s[i] alone and the other is decode s[i] + s[i+1]
            # hence in this case, dp[i] = dp[i+1] + dp[i+2]
            # if s[i] is '2', and s[i+1] is '0'~'6', then dp[i] = dp[i+1] + dp[i+2]
            # other situations, dp[i] = dp[i+1] since can only decode alone
                dp[i] = dp[i+1]
                if i < n-1 and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
                    dp[i] = dp[i+1] + dp[i+2]

        return dp[0]