/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  const n = nums.length;
  let max = nums[0];
  let pre = nums[0];

  for (let i = 1; i < n; i++) {
    pre = Math.max(pre + nums[i], nums[i]);
    max = Math.max(max, pre);
  }
  return max;
};

nums = [1];
console.log(maxSubArray(nums));
