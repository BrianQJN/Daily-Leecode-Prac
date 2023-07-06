"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example:
Input: nums = [1,3,4,2,2]
Output: 2
"""
class Solution:
    def findTheDuplicateNumber(self, nums):
        nums = sorted(nums)

        left = 0
        while left < len(nums) - 1:
            if nums[left] == nums[left+1]:
                return nums[left]
            left += 1

    def findTheDuplicateNumber2(self, nums):
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


if __name__ == "__main__":
    print(Solution.findTheDuplicateNumber2(Solution, [1,3,4,2,2]))