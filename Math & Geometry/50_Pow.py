"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000
"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # if n is negative, we invert x and negate n for calculation
        if n < 0:
            x = 1 / x
            n = -n
        
        return self.power(x, n)
        
    def power(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        # if n is even, we can convert x^n to (x^(n/2))^2 to reduce calculation times
        # if n is odd, we can convert x^n to ((x^((n-1)/2))^2)*x to reduce calculation times
        half = self.power(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x