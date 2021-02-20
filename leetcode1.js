/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) return [i, j];
    }
  }
};

// solution2 : hashTable
var twoSum = function (nums, target) {
  const hashTable = new Map();
  for (let i = 0; i < nums.length; i++) {
    if (hashTable.has(target - nums[i])) return [hashTable.get(target - nums[i]), i];
    hashTable.set(nums[i], i);
  }
};
