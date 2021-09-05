/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isBalanced = function (root) {
  const getHeight = (root) => {
    if (!root) return 0;

    const { left, right } = root;
    const leftHeight = getHeight(left);
    const rightHeight = getHeight(right);

    if (
      leftHeight === -1 ||
      rightHeight === -1 ||
      Math.abs(leftHeight - rightHeight) > 1
    ) {
      return -1;
    } else {
      return Math.max(leftHeight, rightHeight) + 1;
    }
  };

  return getHeight(root) >= 0;
};
