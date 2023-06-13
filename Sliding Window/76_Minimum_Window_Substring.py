"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
"""
class Solution(object):
    def minimumWindowSubstring(self, s, t):
        if s == "" or t == "":
            return ""
        
        window, countT = {}, {}

        for char in t:
            countT[char] = countT.get(char, 0) + 1
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            char = s[r]

            window[char] = window.get(char, 0) + 1

            if char in countT and window[char] == countT[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res

        return s[l:r+1] if resLen != float("infinity") else ""
    

if __name__ == "__main__":
    test = Solution
    # print(test.minimumWindowSubstring(test, "ADOBECODEBANC", "ABC"))
    print(test.minimumWindowSubstring(test, "aa", "aa"))