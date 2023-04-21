"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        head = 0
        head_index = 0
        cur_list = []
        sub_list = []
        remain = 0

        for num in nums:
            head = num
            remain = target - head
            cur_list = nums[head_index:]
            sub_list = cur_list[1:]
            sub_index = 0

            for sub_num in sub_list:
                if sub_num != remain:
                    sub_index += 1
                    continue
                else:
                    output.append(head_index)
                    output.append(sub_index + head_index + 1)
                    return output
            
            head_index += 1

        return output
    

if __name__ == "__main__":
    test = Solution
    print(test.twoSum(test, [2,7,11,15], 9))
    print(test.twoSum(test, [3,2,4], 6))
    print(test.twoSum(test, [3, 3], 6))