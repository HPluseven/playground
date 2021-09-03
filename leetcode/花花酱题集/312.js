/**
 * @param {number[]} nums
 * @return {number}
 */
var maxCoins = function (nums) {
  const vals = Array.prototype.concat(1, nums, 1);
  const n = vals.length;
  const memo = new Array(n).fill(-1).map(() => new Array(n).fill(-1));

  const solve = (left, right) => {
    if (left + 1 >= right) return 0;

    if (memo[left][right] !== -1) return memo[left][right];

    for (let middle = left + 1; middle < right; middle++) {
      let total = vals[left] * vals[middle] * vals[right];
      total += solve(left, middle) + solve(middle, right);
      memo[left][right] = Math.max(total, memo[left][right]);
    }
    return memo[left][right];
  };

  return solve(0, n - 1);
};

console.log(maxCoins([3, 1, 5, 8]));
