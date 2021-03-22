/**
 * @param {number[]} nums
 * @return {number}
 */
var maxCoins = function (nums) {
  const n = nums.length;
  const vals = Array.prototype.concat(1, nums, 1);
  const rec = Array(n + 2);
  for (let i = 0; i < rec.length; i++) {
    rec[i] = Array(n + 2).fill(-1);
  }

  const solve = (left, right) => {
    if (left >= right - 1) {
      return 0;
    }
    if (rec[left][right] != -1) {
      return rec[left][right];
    }
    for (let i = left + 1; i < right; i++) {
      let sum = vals[left] * vals[i] * vals[right];
      sum += solve(left, i) + solve(i, right);
      rec[left][right] = Math.max(rec[left][right], sum);
    }
    return rec[left][right];
  };
  return solve(0, n + 1);
};

const nums = [3, 1, 5, 8];
console.log(maxCoins(nums));
