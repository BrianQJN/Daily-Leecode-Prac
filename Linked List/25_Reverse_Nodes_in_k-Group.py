"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseNodesInKGroup(self, head, k):
        dummy = ListNode()
        tail = dummy

        while True:
            count = k
            stack = []
            tmp = head
            while tmp and count > 0:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1
                
            if count:
                tail.next = head
                break

            while stack:
                tail.next = stack.pop()
                tail = tail.next
            
            tail.next = tmp
            head = tmp
        
        return dummy.next