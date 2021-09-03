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
 * @param {number} targetSum
 * @return {number[][]}
 */
var pathSum = function (root, targetSum) {
  const ans = [];
  const dfs = (root, targetSum, path) => {
    if (!root) return;

    const { left, right, val } = root;
    path.push(val);
    if (!left && !right && val === targetSum) ans.push(path.slice());
    dfs(left, targetSum - val, path);
    dfs(right, targetSum - val, path);
    path.pop();
  };

  dfs(root, targetSum, []);
  return ans;
};
