"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""
import collections

class Solution(object):
    def slidingWindowMaximum(self, nums, k):
        if not nums or not k:
            return []

        if len(nums) == 1 or k == 1:
            return nums
        
        queue = []
        res = []
        l = r = 0

        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            if l > queue[0]:
                queue.pop(0)
            
            if (r + 1) >= k:
                res.append(nums[queue[0]])
                l += 1
            
            r += 1
        return res

if __name__ == '__main__':
    test = Solution
    print(test.slidingWindowMaximum(test, [1,3,-1,-3,5,3,6,7], 3))
