"""
Given a binary tree, determine if it is height-balanced.

Example:
Input: root = [3,9,20,null,null,15,7]
Output: true
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balancedBinaryTree(self, root):
        def height(node: TreeNode) -> int:
            # 如果节点为空，高度为0
            if not node:
                return 0
            # 递归计算左子树和右子树的高度，并取较大值加1作为当前节点的高度
            return max(height(node.left), height(node.right)) + 1

        # 如果根节点为空，说明是空树，返回True
        if not root:
            return True

        # 检查当前节点的左子树和右子树的高度差是否小于等于1，
        # 同时递归地检查左子树和右子树是否都是平衡的
        return (
            abs(height(root.left) - height(root.right)) <= 1 and
            self.isBalanced(root.left) and
            self.isBalanced(root.right)
        )