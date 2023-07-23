"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

Example:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
"""
from collections import Counter, deque
import heapq


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # initialize the maxHeap and invert the tasks to its count
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        # initialize the deque to record [(-cnt, next available time)]
        queue = deque()
        
        # initialize the time record
        time = 0

        # if maxHeap or queue is not empty, means that there are still some tasks to be executed
        while maxHeap or queue:
            time += 1

            if not maxHeap:
                time = queue[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    queue.append([cnt, time + n])
            
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])

        return time
