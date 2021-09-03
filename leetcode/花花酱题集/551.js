/**
 * @param {string} s
 * @return {boolean}
 */
var checkRecord = function (s) {
  let aNums = 0;
  let lNums = 0;

  for (const char of s) {
    if (char === "L") {
      lNums++;
    } else {
      lNums = 0;
    }
    if (char === "A") {
      aNums++;
    }
    if (aNums === 2 || lNums >= 3) {
      return false;
    }
  }
  return true;
};
