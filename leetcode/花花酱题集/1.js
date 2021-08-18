/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const hashTable = new Map();
  for (let i = 0; i < nums.length; i++) {
    if (hashTable.has(target - nums[i]))
      return [hashTable.get(target - nums[i]), i];
    hashTable.set(nums[i], i);
  }
};

const nums = [2, 7, 11, 15];
const target = 9;
console.log(twoSum(nums, target));
