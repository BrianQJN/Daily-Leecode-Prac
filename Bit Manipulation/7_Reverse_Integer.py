"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        flag = False

        if x < 0:
            flag = True
            x = -x

        while x > 0:
            # extract the last digit
            tmp = x % 10
            res = res * 10 + tmp
            x //= 10
        
        if flag:
            res = -res

        return res if -2147483648 < res < 2147483647 else 0