"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.
"""
class Solution(object):
    def longestRepeatingCharacterReplacement(self, s, k):
        res = 0
        left = 0
        count = {}

        for right in range(0, len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)

        return res
    

if __name__ == '__main__':
    test = Solution
    print(test.longestRepeatingCharacterReplacement(test, "AABABBA", 1))
    