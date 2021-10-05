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
 * @return {number[][]}
 */
var levelOrder = function (root) {
  if (!root) return [];

  const res = [];
  const queue = [root];

  while (queue.length > 0) {
    const n = queue.length;
    const temp = [];
    for (let i = 0; i < n; i++) {
      const { left, right, val } = queue.shift();
      temp.push(val);
      if (left) queue.push(left);
      if (right) queue.push(right);
    }
    res.push(temp);
  }
  return res;
};
