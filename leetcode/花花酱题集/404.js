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
 * @return {number}
 */
var sumOfLeftLeaves = function (root) {
  let sum = 0;

  (function (root) {
    if (!root) return;
    const { left, right } = root;
    if (left && !left.left && !left.right) sum += left.val;

    arguments.callee(left);
    arguments.callee(right);
  })(root);
  return sum;
};
