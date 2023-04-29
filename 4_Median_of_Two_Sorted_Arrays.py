"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n))

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
class Solution(object):
    def medianOfTwoSortedArray(self, nums1, nums2):
        p1 = 0
        p2 = 0
        nums = []
        m = len(nums1)
        n = len(nums2)
        median = 0

        if m == 0 and n != 0:
            nums = nums2
        elif m != 0 and n == 0:
            nums = nums1
        else:
            while p1 != m-1 and p2 != n-1:
                if nums1[p1] > nums2[p2]:
                    nums.append(nums2[p2])
                    p2 += 1
                elif nums1[p1] < nums2[p2]:
                    nums.append(nums1[p1])
                    p1 += 1
                else:
                    nums.append(nums1[p1])
                    nums.append(nums2[p2])
                    p1 += 1
                    p2 += 1
            if p1 == m-1 and p2 != n-1:
                while p2 < n:
                    if nums1[p1] > nums2[p2]:
                        nums.append(nums2[p2])
                        p2 += 1
                    elif nums1[p1] == nums2[p2]:
                        nums.append(nums2[p2])
                        nums.append(nums1[p1])
                        p2 += 1
                        break
                    else:
                        nums.append(nums1[p1])
                        break
                for num in nums2[p2:]:
                    nums.append(num)
            elif p1 != m-1 and p2 == n-1:
                while p1 < m:
                    if nums2[p2] > nums1[p1]:
                        nums.append(nums1[p1])
                        p1 += 1
                    elif nums1[p1] == nums2[p2]:
                        nums.append(nums2[p2])
                        nums.append(nums1[p1])
                        p1 += 1
                        break
                    else:
                        nums.append(nums2[p2])
                        break
                for num in nums1[p1:]:
                    nums.append(num)
            else:
                if nums1[p1] > nums2[p2]:
                    nums.append(nums2[p2])
                    nums.append(nums1[p1])
                elif nums1[p1] == nums2[p2]:
                    nums.append(nums2[p2])
                    nums.append(nums1[p1])
                else:
                    nums.append(nums1[p1])
                    nums.append(nums2[p2])

        if (m+n)%2 == 0:
            median = (nums[int((m+n)/2)] + nums[int((m+n)/2-1)])/2
        else:
            median = nums[int((m+n+1)/2 - 1)]

        return median

            
if __name__ == "__main__":
    test = Solution
    print(test.medianOfTwoSortedArray(test, nums1 = [1,3], nums2 = [2]))
    print(test.medianOfTwoSortedArray(test, nums1 = [1,2], nums2 = [3,4]))