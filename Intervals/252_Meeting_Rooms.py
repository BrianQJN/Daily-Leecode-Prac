"""
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
"""
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return True
        
        # sort intervals in ascending order by start-i
        intervals.sort(key=lambda x: x[0])
        end = intervals[0][1]

        # traverse the intervals
        for i in range(1, len(intervals)):
            # if there is overlap, return False
            if intervals[i][0] < end:
                return False
            
            # else update the end to cur interval's end-i
            end = intervals[i][1]

        return True