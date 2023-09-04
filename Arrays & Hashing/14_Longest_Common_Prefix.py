"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        # initialize the prefix as first str
        prefix = strs[0]

        # traverse the strs from the second one
        for i in range(1, len(strs)):
            # if cur str is not start with the common prefix
            while not strs[i].startswith(prefix):
                # short the prefix
                prefix = prefix[:-1]
                # if prefix is empty, return empty string
                if not prefix:
                    return ""
        
        return prefix