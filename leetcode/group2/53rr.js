/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  let pre = -Infinity;
  let maxAns = nums[0];

  for (const num of nums) {
    pre = Math.max(pre + num, num);
    maxAns = Math.max(pre, maxAns);
  }
  return maxAns;
};

// 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
// 输出：6
// 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

const nums = [-2,1,-3,4,-1,2,1,-5,4]
console.log(maxSubArray(nums));
