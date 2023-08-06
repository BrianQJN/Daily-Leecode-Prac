"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
"""
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # sort intervals to ascending order based on the end-i of each interval
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        count = 0

        for i in range(1, len(intervals)):
            cur_interval = intervals[i]

            # if there is overlap, delete cur interval, because it has larger end
            # to give more space to intervals, we need to remove the larger end interval
            if cur_interval[0] < end:
                count += 1
                continue

            # if there is no overlap, update the end to cur interval's end
            end = cur_interval[1]

        return count
            