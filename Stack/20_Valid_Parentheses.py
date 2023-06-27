"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "([)]"
Output: flase
"""
class Solution(object):
    def validParentheses(self, s):
        parentheses_map = {']':'[', '}':'{', ')':'('}
        stack = []

        for char in s:
            if char not in parentheses_map:
                stack.append(char)
                continue
            if not stack or parentheses_map[char] != stack[-1]:
                return False
            stack.pop()
        
        return not stack


if __name__ == '__main__':
    test = Solution
    print(test.validParentheses(test, "([)]"))
    print(test.validParentheses(test, "(())"))
    print(test.validParentheses(test, "([)]"))