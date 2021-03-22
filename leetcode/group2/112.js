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
  const ret = [];
  const ans = [];

  const dfs = (node, targetSum) => {
    if (!node) {
      return;
    }

    const { left, right, val } = node;

    if (val === targetSum && !left && !right) {
      ans.push(val);
      ret.push(ans.slice());
      ans.pop();
      return;
    }

    if (left) {
      ans.push(val);
      dfs(left, targetSum - val);
      ans.pop();
    }
    if (right) {
      ans.push(val);
      dfs(right, targetSum - val);
      ans.pop();
    }
  };

  dfs(root, targetSum);

  return ret;
};

// improve
var pathSum = function (root, targetSum) {
  const ret = [];
  const ans = [];

  const dfs = (node, targetSum) => {
    if (!node) {
      return;
    }
    const { left, right, val } = node;
    ans.push(val);
    if (val === targetSum && !left && !right) {
      ret.push(ans.slice());
    }
    dfs(left, targetSum - val);
    dfs(right, targetSum - val);
    ans.pop();
  };

  dfs(root, targetSum);
  return ret;
};
