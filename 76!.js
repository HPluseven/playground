/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */

// time out
// var minWindow = function (s, t) {
//   if (s.length < t.length) return "";
//   let windowSize = t.length;

//   while (windowSize <= s.length) {
//     let left = 0;
//     let lookup = s.substring(left, windowSize);
//     if (isOverride(lookup, t)) return s.substring(left, windowSize);
//     for (let i = windowSize; i < s.length; i++) {
//       lookup = lookup.substring(1);
//       left++;
//       lookup += s[i];
//       if (isOverride(lookup, t)) return s.substring(left, i + 1);
//     }
//     windowSize++;
//   }
//   return "";
// };

// let isOverride = function (lookup, t) {
//   for (const char of t) {
//     if (!lookup.includes(char)) {
//       return false;
//     }
//     lookup = lookup.replace(char, "");
//   }
//   return true;
// };

// refer
/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function (s, t) {
  const need = {};
  for (const c of s) {
    need[c] = 0;
  }
  for (c of t) {
    if (need[c]) need[c]++;
    else need[c] = 1;
  }
  let needCnt = t.length;
  let left = 0;
  let res = [0, Infinity];

  for (let right = 0; right < s.length; right++) {
    const c = s[right];
    if (need[c] > 0) needCnt--;
    need[c]--;
    if (needCnt === 0) {
      while (true) {
        let c = s[left];
        if (need[c] === 0) break;
        need[c]++;
        left++;
      }
      if (right - left < res[1] - res[0]) res = [left, right];
      need[s[left]]++;
      left++;
      needCnt++;
    }
  }
  return res[1] > s.length ? "" : s.substring(res[0], res[1] + 1);
};

let s = "a";
let t = "aa";
console.log(minWindow(s, t));
