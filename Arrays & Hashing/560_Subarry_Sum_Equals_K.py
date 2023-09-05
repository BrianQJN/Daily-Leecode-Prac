"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
"""
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # initialize the prefix_sum map to record the frequencies a prefix sum appears
        prefix_sum = {0: 1}
        sum_count = 0
        prefix_sum_value = 0

        for num in nums:
            # update the prefix_sum
            prefix_sum_value += num
            # if the subtraction is existed in the prefix_sum, add the frequency the prefix sum appears
            if prefix_sum_value - k in prefix_sum:
                sum_count += prefix_sum[prefix_sum_value-k]
            if prefix_sum_value in prefix_sum:
                prefix_sum[prefix_sum_value] += 1
            else:
                prefix_sum[prefix_sum_value] = 1

        return sum_count