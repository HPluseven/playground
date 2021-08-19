/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
var findContentChildren = function (g, s) {
  g.sort((x, y) => x - y);
  s.sort((x, y) => x - y);
  let res = 0;
  let i = 0;
  let j = 0;

  while (i < g.length && j < s.length) {
    if (g[i] <= s[j]) {
      i++;
      res++;
    }
    j++;
  }
  return res;
};

g = [10, 9, 8, 7];
s = [5, 6, 7, 8];

console.log(findContentChildren(g, s));

7, 8, 9, 10;
5, 6, 7, 8;
