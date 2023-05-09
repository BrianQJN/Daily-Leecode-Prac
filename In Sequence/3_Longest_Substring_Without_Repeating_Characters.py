"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring
"""
class Solution(object):
    def longestSubstring(self, s):
        max_len = 1
        cur_len = 0
        index = 0

        if not s:
            return 0

        for char in s:
            cur_substring = []
            if char not in cur_substring:
                cur_substring.append(char)
                if len(s[index+1:]) != 1:
                    for sub_char in s[index+1:]:
                        if sub_char not in cur_substring:
                            cur_substring.append(sub_char)
                        else:
                            cur_len = len(cur_substring)
                            if cur_len > max_len:
                                max_len = cur_len
                            break
                else:
                    if s[index+1:][0] not in cur_substring:
                        cur_substring.append(s[index+1:][0])
                cur_len = len(cur_substring)
                if cur_len > max_len:
                    max_len = cur_len
                index += 1
        return max_len


if __name__ == '__main__':
    test = Solution
    print(test.longestSubstring(test, "abcabcbb"))
    print(test.longestSubstring(test, "bbbbb"))
    print(test.longestSubstring(test, "pwwkew"))
    print(test.longestSubstring(test, "bwf"))
