"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them

Example:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3]
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 0

        def getDepth(node):
            if not node:
                return 0
            L = getDepth(node.left)
            R = getDepth(node.right)
            self.ans = max(self.ans, L+R)

            return max(L, R) + 1
        
        getDepth(root)
        
        return self.ans