"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""
class Solution(object):
    def permutationInString(self, s1, s2):
        count1 = {}
        count2 = {}
        left, right = 0, len(s1) - 1

        for char in s1:
            count1[char] = 1 + count1.get(char, 0)

        for char in s2[0:right]:
            count2[char] = 1 + count2.get(char, 0)

        while right < len(s2):
            count2[s2[right]] = 1 + count2.get(s2[right], 0)

            if count1 == count2:
                return True
            
            count2[s2[left]] = count2.get(s2[left], 0) - 1
            if count2[s2[left]] == 0:
                del count2[s2[left]]
            left += 1

            right += 1
        
        return False
    

if __name__ == '__main__':
    test = Solution
    print(test.permutationInString(test, "ab", "eidbaooo"))
    print(test.permutationInString(test, "ab", "eidboaooo"))
    print(test.permutationInString(test, "adc", "dcda"))