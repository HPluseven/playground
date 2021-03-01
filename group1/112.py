# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


class Solution:
    # bfs
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        queue = [(root, root.val)]

        while queue:
            node, path = queue.pop(0)
            if not node.left and not node.right and path == sum:
                return True
            left, right = node.left, node.right
            if left:
                queue.append((left, path+left.val))
            if right:
                queue.append((right, path+right.val))

        return False
