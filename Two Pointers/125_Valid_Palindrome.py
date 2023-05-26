"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Constraints:
1 <= s.length <= 2 * 10**5
s consists only of printable ASCII characters.
"""
class Solution(object):
    def validPalindrome(self, s):
        temp = []
        for char in s:
            if char.isalnum() or char.isalpha():
                temp.append(char.lower())
        
        return True if temp == temp[::-1] else False
    

if __name__ == "__main__":
    test = Solution
    print(test.validPalindrome(test, "A man, a plan, a canal: Panama"))
    print(test.validPalindrome(test, "a121A"))
    print(test.validPalindrome(test, "a"))