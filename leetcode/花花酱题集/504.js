/**
 * @param {number} num
 * @return {string}
 */
var convertToBase7 = function (num) {
  if (num === 0) {
    return num.toString();
  }

  const negative = num > 0 ? false : true;
  let numAbs = Math.abs(num);
  let ans = "";

  while (numAbs > 0) {
    ans = (numAbs % 7) + ans;
    numAbs = parseInt(numAbs / 7);
  }
  return negative ? "-" + ans : ans;
};

console.log(convertToBase7(0));
