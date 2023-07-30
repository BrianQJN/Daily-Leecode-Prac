"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visited = set()

        # build the directed graph
        graph = {i: [] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        # define the dfs
        def dfs(course):
            # if the course has been visited in the current dfs, means there is a cycle
            # so it means there is a cycle prerequisites
            if course in visited:
                return False
            
            # mark the course as visited
            visited.add(course)

            # call dfs on all prerequisites
            for prerequisite in graph[course]:
                # if there is a cycle prerequisites in cur course's prerequisite course, means a cycle prerequisites
                if dfs(prerequisite) == False:
                    return False

            # when finishing the dfs path, remove the course from the visited
            visited.remove(course)

            return True
        
        # start dfs from every course
        for course in range(numCourses):
            if not dfs(course):
                return False
            
        return True