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
 * @return {string[][]}
 */
var printTree = function (root) {
  const getTreeLength = (root) => {
    if (!root) return 0;

    const { left, right } = root;

    if (left && right) {
      return 1 + Math.max(getTreeLength(left), getTreeLength(right));
    } else if (left) {
      return 1 + getTreeLength(left);
    } else if (right) {
      return 1 + getTreeLength(right);
    } else {
      return 1;
    }
  };
  const m = getTreeLength(root);
  const n = 2 ** m - 1;
  const ans = new Array(m).fill(0).map(() => new Array(n).fill(""));

  const filledTree = (root, m, start, end) => {
    if (!root) return;

    const { left, right, val } = root;
    const middle = (start + end) / 2;
    ans[m][middle] = "" + val;

    if (left) filledTree(left, m + 1, start, middle - 1);
    if (right) filledTree(right, m + 1, middle + 1, end);
  };
  filledTree(root, 0, 0, n - 1);
  return ans;
};
