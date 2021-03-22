# import collections
# if __name__ == "__main__":
#     # a = [1, 2, 3, 4]
#     # print(list(reversed(a[0:4])))
#     print(int(3.2))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, nums: list):
        self.root = self.create_tree(nums, 0)

    def create_tree(self, nums: list, idx: int):
        if idx >= len(nums):
            return None

        node = TreeNode(nums[idx])
        node.left = self.create_tree(nums, idx*2+1)
        node.right = self.create_tree(nums, idx*2+2)

        return node

tree = Tree([1,2,3,4]).root
print(tree.val)
print(tree.left.val)
print(tree.right.val)
print(tree.left.left.val)
print(tree.left.left.left)
print(tree.left.right)


