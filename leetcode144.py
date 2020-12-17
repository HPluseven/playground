# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if root:
            # print(root.val)
            result.push(root.val)
            result += self.preorderTraversal(root.left)
            result += self.preorderTraversal(root.right)
        return result