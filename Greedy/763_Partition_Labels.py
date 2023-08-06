"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
"""
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # initialize a dict to record the last index of each char
        last_index = {}
        for i, char in enumerate(s):
            last_index[char] = i

        # initialize the start and end to record the boundary of each part
        start, end = 0, 0
        res = []

        # traverse string s to find the start and end for each part
        for i, char in enumerate(s):
            # update end index for cur part
            end = max(end, last_index[char])

            # when the traverse reach the end index, means we have found a proper part
            if i == end:
                res.append(end - start + 1)
                # update the start index to the next index of end index, i.e. move to next part
                start = end + 1

        return res
