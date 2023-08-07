"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
1² + 9² = 82
8² + 2² = 68
6² + 8² = 100
1² + 0² + 0² = 1
"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_next(num):
            # calculate next number of cur num
            total_sum = 0
            while num > 0:
                digit = num % 10
                total_sum += digit * digit
                num //= 10
            return total_sum
        
        # initialize two num pointer
        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            # using fast and slow algorithm, every time slow moves to next sum while fast moves 2 times
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        # the boundary condition of last loop is there is a sum is 1
        # and another condition is that slow and fast pointers would meet, means there is a cycle
        # so we need to determine the result by checki if fast == 1
        return fast == 1