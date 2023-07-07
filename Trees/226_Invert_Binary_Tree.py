"""
Given the root of a binary tree, invert the tree, and return its root.

Example:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertBinaryTree(self, root):
        if not root:
            return None
        
        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)

        return root