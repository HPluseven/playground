# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         if not root:
#             return res

#         def dfs(root):
#             if not root:
#                 return
#             left, right = root.left, root.right
#             if left:
#                 dfs(left)
#             res.append(root.val)
#             if right:
#                 dfs(right)
#         dfs(root)

#         return res
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         if not root:
#             return res
#         stack = []
#         p = root

#         while(p or stack):
#             if p:
#                 stack.append(p)
#                 p = p.left
#             else:
#                 p = stack.pop()
#                 res.append(p.val)
#                 p = p.right
#         return res

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = [(False, root)]
        while stack:
            visited, node = stack.pop()
            if not node:
                continue
            if visited:
                res.append(node.val)
            else:
                stack.append((False, node.right))
                stack.append((True, node))
                stack.append((False, node.left))

        return res
