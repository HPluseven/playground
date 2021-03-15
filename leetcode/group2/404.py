# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        left, right = root.left, root.right
        if left and not left.left and not left.right:
            return left.val + self.sumOfLeftLeaves(right)

        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
