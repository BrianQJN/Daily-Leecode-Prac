"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
"""
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) == 1:
            return nums
        
        # split the array to two parts
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        # split each part to two parts
        left = self.sortArray(left)
        right = self.sortArray(right)

        return self.merge(left, right)


    def merge(self, left, right):
        res = []
        left_idx, right_idx = 0, 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                res.append(left[left_idx])
                left_idx += 1
            else:
                res.append(right[right_idx])
                right_idx += 1
        
        res += left[left_idx:]
        res += right[right_idx:]

        return res