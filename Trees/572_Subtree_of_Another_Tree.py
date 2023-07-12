"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root, subRoot):
        # if both are null, return True
        if not root and not subRoot:
            return True
        # if one of them are null, return False
        if not root or not subRoot:
            return False
        
        # if they are not null, we need to determine:
        # 1. in the current node they are the same tree
        # 2. or subRoot is the same tree in root's left children tree
        # 3. or subRoot is the same tree in root's right children tree
        return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
    
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        
        if s and t and s.val == t.val:
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
        else:
            return False