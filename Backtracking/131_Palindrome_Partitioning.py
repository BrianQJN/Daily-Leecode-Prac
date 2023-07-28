"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Example:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
"""
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []

        def is_palindrome(s):
            """
            check if the string is a palindrom string
            """
            return s == s[::-1]
        
        def dfs(start, cur):
            # if we have traversed all the char in the string, append the cur partition
            if start == len(s):
                res.append(cur[:])
                return
            
            # traverse all possible substrings from the index start
            for end in range(start+1, len(s)+1):
                substring = s[start:end]
                # if cur substring is palindrome, add it to the cur and call the dfs function recursively
                if is_palindrome(substring):
                    cur.append(substring)
                    dfs(end, cur)
                    # backtracking, pop the added substring
                    cur.pop()

        dfs(0, [])

        return res
            
