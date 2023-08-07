"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
"""
import heapq


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # sort intervals in ascending order by start-i
        intervals.sort(key=lambda x: x[0])
        
        # use a heap to record the meeting rooms are currently using
        room_heap = []
        heapq.heappush(room_heap, intervals[0][1])

        # traverse the intervals
        for i in range(1, len(intervals)):
            cur_interval = intervals[i]

            # if there is no overlap between cur_interval and last meeting room time
            if room_heap[0] <= cur_interval[0]:
                heapq.heappop(room_heap)
            heapq.heappush(room_heap, cur_interval[1])

        return len(room_heap)