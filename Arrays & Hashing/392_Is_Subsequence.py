"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # initialize two pointers
        i, j = 0, 0

        # traverse the string s and t and do the matching
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)
    

print(Solution.isSubsequence(Solution, s = "abc", t = "ahbgdc"))
print(Solution.isSubsequence(Solution, s = "axc", t = "ahbgdc"))
print(Solution.isSubsequence(Solution, s = "", t = "ahbgdc"))
print(Solution.isSubsequence(Solution, s = "a", t = ""))