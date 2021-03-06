# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        ans = []
        if not root:
            return ans
        # queue = [(0, root)]

        # while queue:
        #     h, node = queue.pop(0)

        #     while h < len(ans)-1:
        #         ans.append([])

        #     temp = [node.val]
        #     left, right = node.left, node.right
        #     if left or right:
        #     temp = ['', node.val, '']

        #     # if node.left:
        #     #     temp = ['']+temp
        #     #     queue.append(node.left)

        #     # if node.right:
        #     #     temp += ['']
        #     #     queue.append(node.right)

        return ans

        # def dfs(node, h):
        #     if not node:
        #         return

        #     ans[h] += [node.val]
