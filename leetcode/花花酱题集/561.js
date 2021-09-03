/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function (nums) {
  let ans = 0;
  nums.sort((x, y) => x - y);
  for (let i = 0; i < nums.length; i += 2) {
    ans += nums[i];
  }
  return ans;
};

const nums = [6, 2, 6, 5, 1, 2];
console.log(arrayPairSum(nums));
