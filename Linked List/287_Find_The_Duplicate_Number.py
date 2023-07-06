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
        n = len(nums)
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            cnt = sum(num <= mid for num in nums)   # nums中 <=mid 的元素个数
            if cnt <= mid:      # 目标元素在mid右侧
                left = mid+1
            else:
                right = mid
        
        return left

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
    print(Solution.findTheDuplicateNumber(Solution, [1,3,4,2,2]))