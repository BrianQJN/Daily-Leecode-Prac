"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []

        # map the digits to chars
        digit_chars = {
            "2": ['a','b','c'],
            "3": ['d','e','f'],
            "4": ['g','h','i'],
            "5": ['j','k','l'],
            "6": ['m','n','o'],
            "7": ['p','q','r','s'],
            "8": ['t','u','v'],
            "9": ['w','x','y','z']
        }

        def dfs(index, cur):
            # boundary conditions, if the index reach the end of the digits end, add the cur to res
            if index == len(digits):
                res.append(cur)
                return
            
            # get the corresponding chars of cur digit
            chars = digit_chars[digits[index]]

            # for each character, we add it to cur, and call dfs function recursively to get every combination
            for char in chars:
                dfs(index + 1, cur + char)

        if digits:
            dfs(0, '')
        
        return res