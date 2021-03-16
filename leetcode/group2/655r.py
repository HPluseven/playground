# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        height = self.get_height(root)
        ret = [['']*(2**height-1) for _ in range(height)]
        self.fill(ret, root, 0, 0, len(ret[0]))
        return ret

    def fill(self, ret, node, i, l, r):
        if not node:
            return
        ret[i][(l+r)//2] = str(node.val)
        self.fill(ret, node.left, i+1, l, (l+r)//2-1)
        self.fill(ret, node.right, i+1, (l+r)//2+1, r)

    def get_height(self, root):
        if not root:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))
