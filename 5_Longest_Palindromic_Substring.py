"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""
class Solution(object):
    def longestPalindromicSubstring(self, s):
        cur_substr = ""
        max_len = 0
        longest_substr = ""
        pointer = 0
        sub_pointer = 0
        
        if len(s) == 1:
            return s
        else:
            for char in s:
                cur_substr += char
                if char in s[pointer+1:]:
                    for sub_char in s[pointer+1:]:
                        cur_substr += sub_char
                        if cur_substr == cur_substr[::-1]:
                            if len(cur_substr) > max_len:
                                longest_substr = cur_substr
                                max_len = len(cur_substr)
                        sub_pointer += 1
                else:
                    if len(cur_substr) > max_len:
                        longest_substr = cur_substr
                        max_len = len(cur_substr)
                    
                cur_substr = ""
                pointer += 1
        
        return longest_substr
    
    def longestPalindromicSubstring_2(self, s):
        cur_substr = ""
        max_len = 0
        longest_substr = ""
        pointer = 0
        sub_pointer = 0

        if len(s) == 1:
            return s
        else:
            for char in s:
                cur_substr += char
                if char in s[pointer+1:]:
                    for sub_char in s[pointer+1:]:
                        cur_substr += sub_char
                        if cur_substr == cur_substr[::-1]:
                            if len(cur_substr) > max_len:
                                longest_substr = cur_substr
                                max_len = len(cur_substr)
                        if char in s[pointer+1:][sub_pointer+1:]:
                            sub_pointer += 1
                            continue
                        else:
                            break
                else:
                    if len(cur_substr) > max_len:
                        longest_substr = cur_substr
                        max_len = len(cur_substr)

                cur_substr = ""
                pointer += 1
        
        return longest_substr
    

if __name__ == "__main__":
    test = Solution
    print(test.longestPalindromicSubstring_2(test, "babad"))
    print(test.longestPalindromicSubstring_2(test, "cbbd"))
    print(test.longestPalindromicSubstring_2(test, "ccc"))
