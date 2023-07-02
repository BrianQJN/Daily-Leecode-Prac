"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
"""
class Solution(object):
    def findMinInRotatedSortedArray(self, nums):
        left, right = 0, len(nums) - 1
        cur_min = float('inf')

        while left < right:
            mid = (left + right) // 2
            cur_min = min(cur_min, nums[mid])

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        
        return min(cur_min, nums[left])
    

if __name__ == '__main__':
    test = Solution
    print(test.findMinInRotatedSortedArray(test, [3,4,5,1,2]))