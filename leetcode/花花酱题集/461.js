/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var hammingDistance = function (x, y) {
  let res = x ^ y;
  let count = 0;

  // Brian Kernighan 算法
  while (res !== 0) {
    res &= res - 1;
    count++;
  }
  return count;
};

const x = 0;
const y = 2**31-1;
console.log(hammingDistance(x, y));
