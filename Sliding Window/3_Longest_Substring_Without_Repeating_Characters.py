"""
Given a string s, find the length of the longest substring without repeating characters

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring
"""
class Solution(object):
    def longestSubstringWithoutRepeatingChars(self, s):
        substring = set()
        left = 0
        result = 0

        for right in range(0, len(s)):
            while s[right] in substring:
                substring.remove(s[left])
                left += 1
            substring.add(s[right])
            result = max(result, right - left + 1)

        return result
    

if __name__ == "__main__":
    test = Solution
    print(test.longestSubstringWithoutRepeatingChars(test, "abcabcbb"))
    print(test.longestSubstringWithoutRepeatingChars(test, "bbbbbbb"))
    print(test.longestSubstringWithoutRepeatingChars(test, "pwwkew"))
    print(test.longestSubstringWithoutRepeatingChars(test, ""))