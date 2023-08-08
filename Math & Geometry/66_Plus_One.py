"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #initialize carry to 1
        carry = 1

        # traverse the digits from end to start
        for i in range(len(digits)-1, -1, -1):
            # cur digit plus carry
            total = digits[i] + carry

            # if cur digit is less than 10, return the array directly
            if total < 10:
                digits[i] = total
                return digits
            else:
                digits[i] = 0
                carry = 1
        
        # if we have done the traverse, means that the first digit is 9, and we need to add digit
        digits.insert(0, 1)
        return digits