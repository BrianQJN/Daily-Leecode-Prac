"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
"""
from collections import defaultdict, deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # transform wordList to dict, key is the common word, value is the specific words list with the common part
        word_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                common_word = word[0:i] + '*' + word[i+1:]
                word_dict[common_word].append(word)

        # initialize the queue and visited set
        # queue to store cur level words and the len of cur transformation sequence
        # visited set to store visited words
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        # start BFS
        while queue:
            cur_word, sequence_len = queue.popleft()

            for i in range(len(cur_word)):
                common_word = cur_word[0:i] + '*' + cur_word[i+1:]
                for word in word_dict[common_word]:
                    if word == endWord:
                        return sequence_len + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, sequence_len+1))
        
        return 0
