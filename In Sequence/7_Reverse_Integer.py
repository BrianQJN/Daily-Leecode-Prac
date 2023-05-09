"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
"""
class Solution(object):
    def reverseInteger(self, x):
        str_integer = ""
        negative_flag = False
        output = 0

        if -10 < x < 10:
            return x
        else:
            str_integer = str(x)
            if str_integer[0] == '-':
                str_integer = str_integer[1:]
                negative_flag = True

            str_integer = str_integer[::-1]
            if str_integer[0] == '0':
                str_integer = str_integer[1:]
            if len(str_integer) == 1:
                return -int(str_integer) if negative_flag else int(str_integer)
            else:
                last_digit = int(str_integer[len(str_integer)-1])
                rest_digit = int(str_integer[0:len(str_integer)-1])

            if rest_digit > 214748364:
                return 0
            if rest_digit == 214748364 and last_digit > 7:
                return 0
            output = int(str_integer)
            
            if negative_flag:
                return -output
            
            return output
        

if __name__ == '__main__':
    test = Solution
    print(test.reverseInteger(test, 123))
    print(test.reverseInteger(test, -123))