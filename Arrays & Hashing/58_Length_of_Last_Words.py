"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 
Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # delete the space at the end of the string
        s = s.rstrip()
        length = 0

        # traverse the string from end to start
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                break
            length += 1

        return length