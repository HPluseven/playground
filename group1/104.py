# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         def f(root, deep):
#             if root:
#                 deep += 1
#             else:
#                 return deep
#             return max(f(root.left, deep), f(root.right, deep))
#         return f(root, 0)


# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         l = self.maxDepth(root.left) + 1
#         r = self.maxDepth(root.right) + 1

#         return l if l > r else r

# bfs
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         deep = 0
#         if not root:
#             return deep
#         queue = [root]

#         while(queue):
#             deep += 1

#             for _ in range(len(queue)):
#                 p = queue.pop(0)
#                 if p.left:
#                     queue.append(p.left)
#                 if p.right:
#                     queue.append(p.right)
#         return deep

# dfs
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_deep = 0
        if not root:
            return max_deep
        p = root
        deep = 0
        max_deep = 0
        s = []

        while(s or p):
            while(p):
                deep += 1
                s.append((p, deep))
                p = p.left
            p = s[-1][0]
            deep = s[-1][1]
            if deep > max_deep:
                max_deep = deep
            s.pop()
            p = p.right
        return max_deep
