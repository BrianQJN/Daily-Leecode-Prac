"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        
        # initialize a dp array to record whether the 0~ith chars in string s can be segmented in the dictionary
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            # traverse all the substrings of string s, check if they are in the dictionary, and last segment are in the dictionary
            for word in wordDict:
                if s[i - len(word):i] == word and dp[i - len(word)]:
                    dp[i] = True
                    break
        
        # we need to check at the end of the strings to see if it can be segmented in the dictionary
        return dp
    
if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code", "yes"]
    # print(Solution.wordBreak(Solution, s, wordDict))
    print(Solution.wordBreak(Solution, s, wordDict))