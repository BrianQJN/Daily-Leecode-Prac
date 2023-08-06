"""
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

Example 1:
Input: s = "()"
Output: true
"""
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # initialize low, high to record the possible un-match min and max counts for left parenthesis
        low, high = 0, 0

        # traverse the string s
        for char in s:
            # since char is '(', so the un-match counts must add one
            if char == '(':
                low += 1
                high += 1
            # since char is ')', so the un-match counts must minus one, but for min, we need to make sure greater than 0
            elif char == ')':
                low = max(0, low - 1)
                high -= 1
            # since char is '*', so it can be '(' lead to unmatch count add one, can be ')' lead to unmatch count minus one
            elif char == '*':
                low = max(0, low - 1)
                high += 1

            # when max possible unmatch '(' is less than 0, means we have ran out of it, so return False
            if high < 0:
                return False
            
        # after traversing, the unmatch count should be zero
        return low == 0