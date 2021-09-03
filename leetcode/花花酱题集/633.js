/**
 * @param {number} c
 * @return {boolean}
 */
var judgeSquareSum = function (c) {
  for (let i = 0; i * i <= c; i++) {
    const b = Math.sqrt(c - i * i);
    if (b === parseInt(b)) return true;
  }
  return false;
};
