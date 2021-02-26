# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        left, right = root.left, root.right
        if not left and not right:
            return True

        def dfs(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False
            else:
                return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(left, right)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root, root]

        while queue:
            if len(queue) % 2 == 1:
                return False

            right = queue.pop()
            left = queue.pop()

            if not left and not right:
                continue
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False
            else:
                queue.append(left.left)
                queue.append(right.right)
                queue.append(left.right)
                queue.append(right.left)

        return True
