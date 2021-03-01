# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def minDepth(self, root: TreeNode) -> int:
#         deep = 0
#         if not root:
#             return deep

#         queue = [root]
#         while queue:
#             deep += 1

#             for _ in range(len(queue)):
#                 p = queue.pop(0)
#                 if not p.left and not p.right:
#                     return deep
#                 if p.left:
#                     queue.append(p.left)
#                 if p.right:
#                     queue.append(p.right)

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        l = self.minDepth(root.left)
        r = self.minDepth(root.right)

        return min(l, r) + 1 if root.left and root.right else l + r + 1
