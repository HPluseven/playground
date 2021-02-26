# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         res = []
#         if not root:
#             return res

#         queue = [root]
#         while(queue):
#             temp = []
#             for _ in range(len(queue)):
#                 p = queue.pop(0)
#                 temp.append(p.val)
#                 if p.left:
#                     queue.append(p.left)
#                 if p.right:
#                     queue.append(p.right)
#             res.append(temp)

#         return res

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res

        def dfs(idx, root):
            if idx > len(res):
                res.append([])
            left, right = root.left, root.right
            res[idx-1].append(root.val)
            if left:
                dfs(idx+1, left)
            if right:
                dfs(idx+1, right)

        dfs(1, root)
        return res
