"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort intervals to ascending based on start-i of each interval
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            last_interval = res[-1]
            cur_interval = intervals[i]

            # if there is overlapping, merge it
            if last_interval[1] >= cur_interval[0]:
                res[-1][1] = max(last_interval[1], cur_interval[1])
            # no overlap, append cur interval to result
            else:
                res.append(cur_interval)
            
        return res