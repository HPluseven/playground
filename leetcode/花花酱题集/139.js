/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */

// timeout
// var wordBreak = function (s, wordDict) {
//   if (wordDict.includes(s)) return true;

//   for (let i = 1; i < s.length; i++) {
//     const w1 = s.slice(0, i);
//     const w2 = s.slice(i);
//     if (wordBreak(w1, wordDict) && wordBreak(w2, wordDict)) return true;
//   }

//   return false;
// };

/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function (s, wordDict) {
  const wordSet = new Set();
  let maxLength = 0;

  for (const word of wordDict) {
    maxLength = Math.max(word.length, maxLength);
    wordSet.add(word);
  }

  const len = s.length;
  const dp = new Array(len + 1).fill(false);
  dp[0] = true;

  for (let i = 1; i <= len; i++) {
    for (let j = i - 1; j >= 0 && i - j <= maxLength; j--) {
      if (dp[j] && wordSet.has(s.slice(j, i))) {
        dp[i] = true;
        break;
      }
    }
  }
  return dp[len];
};

s = "ab";
wordDict = ["a", "b"];

console.log(wordBreak(s, wordDict));
