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
 * @return {number[]}
 */
var averageOfLevels = function (root) {
  if (!root) return 0;

  const queue = [root];
  const ans = [];

  while (queue.length > 0) {
    const n = queue.length;

    let sum = 0;
    for (let i = 0; i < n; i++) {
      const node = queue.shift();
      const { left, right, val } = node;
      sum += val;
      if (left) queue.push(left);
      if (right) queue.push(right);
    }
    ans.push(sum / n);
  }
  return ans;
};
