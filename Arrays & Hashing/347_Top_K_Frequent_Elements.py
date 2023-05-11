"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 10**5
-10**4 <= nums[i] <= 10**4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""
class Solution(object):
    def topKFrequentElements(self, nums, k):
        count = {}
        res = []

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        count_list = sorted(count.values())
        k_frequent = count_list[len(count_list)-k:]

        for key, val in count.items():
            if val in k_frequent:
                res.append(key)
        
        return res


if __name__ == '__main__':
    test = Solution
    print(test.topKFrequentElements(test, [1,1,1,2,2,3], 2))
    print(test.topKFrequentElements(test, [1,1,1,2,2,3], 1))
    print(test.topKFrequentElements(test, [1], 1))