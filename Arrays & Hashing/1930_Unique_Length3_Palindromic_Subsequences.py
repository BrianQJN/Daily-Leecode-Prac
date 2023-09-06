import collections


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # initialize a set to store the palindromic subsequence
        unique_palindromes = set()
        
        # initialize a set to store the left side chars
        left = set()

        # initialize a counter to store the right side chars and appearance
        right = collections.Counter(s)

        for i in range(len(s)):
            # reduce the cur char from right side chars
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right.pop(s[i])

            # try the 26 possible lowercase letters
            for j in range(26):
                char = chr(ord('a') + j)
                # if the letter in both left and right side, it's a palindrome
                if char in left and char in right:
                    unique_palindromes.add((s[i], char))

            # add cur char to left, and move right
            left.add(s[i])

        return len(unique_palindromes)