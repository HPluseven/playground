/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function (triangle) {
  const n = triangle.length;
  const dp = new Array(n + 1).fill(Infinity);

  dp[1] = triangle[0][0];
  for (const row of triangle.slice(1)) {
    for (let i = row.length - 1; i >= 0; i--) {
      dp[i + 1] = Math.min(dp[i + 1], dp[i]) + row[i];
    }
  }
  return Math.min(...dp);
};

// f(n,i) = min(f(n-1,i) f(n-1,i-1))

const triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]];
// const triangle = [[2], [3, 4]];
console.log(minimumTotal(triangle));
