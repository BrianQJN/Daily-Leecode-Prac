"""
There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are 
sorted lexicographically by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
"""
from collections import defaultdict, deque


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = defaultdict(list)
        indegree = {}

        # initialize indegree for all chars
        for word in words:
            for char in word:
                indegree[char] = 0

        # build graph and update indegree
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            min_len = min(len(word1), len(word2))

            for j in range(min_len):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    indegree[word2[j]] += 1
                    break
                return ""

        # initialize the queue with chars that have 0 indegree
        queue = deque([char for char in indegree if indegree[char] == 0])
        res = []

        # perform the topological sort
        while queue:
            char = queue.popleft()
            res.append(char)
            
            for neighbor in graph[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # check if all chars are included in the result
        if len(res) != len(indegree):
            return ""
        
        return ''.join(res)