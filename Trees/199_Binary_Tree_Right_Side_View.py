"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreeRightSideView(self, root):
        # if root is empty, return []
        if not root:
            return []
        
        res = []
        queue = [root]

        while queue:
            size = len(queue)

            res.append(queue[size-1].val)
            for i in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res