# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return 0
        queue = [root]
        ret = []

        while queue:
            n = len(queue)
            sum_ = 0
            for _ in range(n):
                node = queue.pop(0)
                sum_ += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ret.append(sum_/n)

        return ret
