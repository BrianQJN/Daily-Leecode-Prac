"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
"""
from collections import deque


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        res = []
        # count number of prerequisites of each course, and construct directed graph
        prerequisite_count = [0] * numCourses
        graph = {i: [] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            prerequisite_count[course] += 1
            graph[prerequisite].append(course)

        # add the course without prerequisites into deque
        queue = deque([course for course in range(numCourses) if prerequisite_count[course] == 0])

        while queue:
            course = queue.popleft()
            res.append(course)
            numCourses -= 1
            # traverse every course that need this course as prerequisite
            for next_course in graph[course]:
                # redue the number of prerequisites the next course needs
                prerequisite_count[next_course] -= 1
                # if the prerequisites count become 0, add it to the queue
                if prerequisite_count[next_course] == 0:
                    queue.append(next_course)
        
        # if every course is processed, numCourses would be 0, return True. Otherwise, there is a cycle, return False
        return res if numCourses == 0 else []