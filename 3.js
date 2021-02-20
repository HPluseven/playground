/**
 * @param {string} s
 * @return {number}
 */


//  滑动窗口
var lengthOfLongestSubstring = function (s) {
  if (!s) return 0
  const lookup = new Set();
  let left = 0;
  let ans = 0;
  let cur_len = 0;

  for (let i = 0; i < s.length; i++) {
    cur_len++;
    while (lookup.has(s[i])) {
      lookup.delete(s[left]);
      left++;
      cur_len--;
    }
    ans = Math.max(ans, i - left + 1);
    lookup.add(s[i]);
  }
  return ans;
};
