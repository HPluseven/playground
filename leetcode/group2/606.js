/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} t
 * @return {string}
 */
var tree2str = function (t) {
  if (!t) {
    return "";
  }

  let ret = "" + t.val;
  const leftStr = tree2str(t.left);
  const rightStr = tree2str(t.right);

  if (rightStr) {
    ret += "(" + leftStr + ")";
    ret += "(" + rightStr + ")";
  } else if (leftStr) {
    ret += "(" + leftStr + ")";
  }

  return ret;
};

var tree2str = function (t) {
  if (!t) {
    return "";
  }

  if (!t.left && !t.right) {
    return "" + t.val;
  }
  if (!t.right) {
    return t.val + "(" + tree2str(t.left) + ")";
  }
  return t.val + "(" + tree2str(t.left) + ")(" + tree2str(t.right) + ")";
};
