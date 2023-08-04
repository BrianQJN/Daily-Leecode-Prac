"""
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

Example 1:
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
"""
from collections import Counter


class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        n = len(hand)
        # if the length of the hand is not a multiple of groupSize, means we can't divided it into several same length groups
        if n % groupSize != 0:
            return False
        
        # sort the hand list and count the numbers in it
        hand.sort()
        count = Counter(hand)

        # traverse the hand list
        for x in hand:
            # if the number count is 0, means we have ran out of it, so we can skip it
            if count[x] == 0:
                continue
            # for the number, we let it as the start of a group, so if we want it to be a consecutive group
            # we need num, num+1, .... , num + groupSize - 1
            for num in range(x, x+groupSize):
                # if the number we need has ran out, return False, else minus one on its count
                if count[num] == 0:
                    return False
                count[num] -= 1
        
        return True