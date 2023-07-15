"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreeLevelOrderTraversal(self, root):
        # if root is empty, return []
        if not root:
            return []
        
        res = []
        queue = [root]

        while queue:
            # get the lenth of the queue to get the number of nodes in this level
            size = len(queue)
            tmp = []

            for i in range(size):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        
        return res
                
            
