"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 10**5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""
class Solution(object):
    def productOfArrayExceptSelf(self, nums):
        prefix, suffix, res = [1], [1], []
        tmp = 1

        for num in nums:
            tmp *= num
            prefix.append(tmp)
        
        tmp = 1
        for i in range(len(nums)):
            tmp *= nums[len(nums) - i -1]
            suffix.append(tmp)
        
        prefix = prefix[0:len(prefix)-1]
        suffix = suffix[::-1][1:]

        for i in range(len(nums)):
            res.append(prefix[i]*suffix[i])
        
        return res


if __name__ == '__main__':
    test = Solution
    print(test.productOfArrayExceptSelf(test, [1,2,3,4]))
    print(test.productOfArrayExceptSelf(test, [-1,1,0,-3,3]))
