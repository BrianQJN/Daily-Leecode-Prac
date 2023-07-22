"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
"""
import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [-num for num in nums]

        heapq.heapify(nums)

        for i in range(k):
            smallest = heapq.heappop(nums)
            if i == k - 1:
                return -smallest
            
    def partition(self, nums, left, right):
        """
        Using this function, you can get the array that the elements at the left of the nums[left] are less than nums[left] while
        the elements at the right of the nums[left] are greater than nums[left]
        """
        # select the most left element as the pivot
        pivot = nums[left]

        # using double pointers
        l, r = left, right

        while l < r:
            # find the first element less than the pivot from right
            while l < r and nums[r] >= pivot:
                r -= 1
            nums[l] = nums[r]

            # find the first element greater than the pivot from left
            while l < r and nums[l] <= pivot:
                l += 1
            nums[r] = nums[l]

        # put the pivot to the position where the left pointer is equal to the right pointer
        nums[l] = pivot

        # return l is the same as return r, because l == r
        return l
    
