# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         result = []
#         if root:
#             # print(root.val)
#             result.push(root.val)
#             result += self.preorderTraversal(root.left)
#             result += self.preorderTraversal(root.right)
#         return result

# 非递归
class Solution:
   def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
        return result