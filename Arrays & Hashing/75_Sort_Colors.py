"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""
class Solution:
    def BubbleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # Bubble sort function
        for i in range(n):
            for j in range(1, n - i):
                if nums[j] > nums[j - 1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]

    def sortColors(self, nums: list[int]) -> None:
        # low represents next index of 0, high represents next index of 2
        low = 0
        high = len(nums) - 1
        current = 0

        # traverse the array nums:
        while current <= high:
            if nums[current] == 0:
                nums[current], nums[low] = nums[low], nums[current]
                low += 1
                current += 1
            elif nums[current] == 2:
                nums[current], nums[high] = nums[high], nums[current]
                high -= 1
            else:
                current += 1