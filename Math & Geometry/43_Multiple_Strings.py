"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"
"""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1, n2 = len(num1), len(num2)
        # initialize an array res to record the product of two digits
        # and it's obvious, for n1 * n2, the max len of product will be n1 + n2 
        res = [0] * (n1 + n2)

        # traverse num1 and num2, calculate the multiply res in each digit
        for i in range(n1 - 1, -1 , -1):
            for j in range(n2 - 1, -1, -1):
                # calculate the cur digit product
                tmp = int(num1[i]) * int(num2[j])
                # calculate the total with cur digit product and last res
                total = tmp + res[i + j + 1]

                # update the cur digit
                res[i + j + 1] = total % 10
                # add the carry to the next digit
                res[i + j] += total // 10

        # convert the res to a string and remove the leading 0
        res = "".join(map(str, res))
        res = res.lstrip('0')

        return res if res else '0'