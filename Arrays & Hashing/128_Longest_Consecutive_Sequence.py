"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 10**5
-10**9 <= nums[i] <= 10**9
"""
class Solution(object):
    def longestConsecutiveSequence(self, nums):
        longest = 0
        cur_len = 0
        numSet = set(nums)
                
        for num in numSet:
            if (num - 1) in numSet:
                continue
            else:
                cur_len = 1
                while (num+cur_len) in numSet:
                    cur_len += 1
                longest = max(cur_len, longest)
        
        return longest
    

if __name__ == "__main__":
    test = Solution
    print(test.longestConsecutiveSequence(test, [100,4,200,1,3,2]))
    print(test.longestConsecutiveSequence(test, [0,3,7,2,5,8,4,6,0,1]))
    print(test.longestConsecutiveSequence(test, []))