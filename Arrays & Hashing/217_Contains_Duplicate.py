"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Constraints:
1 <= nums.length <= 10**5
-10**9 <= nums[i] <= 10**9
"""
class Solution(object):
    def containsDuplicates(self, nums):
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
    

if __name__ == '__main__':
    test = Solution
    print(test.containsDuplicates(test, [1,2,3,1]))