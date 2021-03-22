/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function (triangle) {
  const n = triangle.length;
  path = [];
  for (let i = 1; i <= n; i++) {
    path.push(Array(i).fill(Infinity));
  }
  path[0][0] = triangle[0][0];
  for (let i = 1; i < n; i++) {
    for (let j = 0; j <= i; j++) {
      if (j === 0) {
        path[i][j] = path[i - 1][j] + triangle[i][j];
      } else if (j === i) {
        path[i][j] = path[i - 1][j - 1] + triangle[i][j];
      } else {
        path[i][j] =
          Math.min(path[i - 1][j], path[i - 1][j - 1]) + triangle[i][j];
      }
    }
  }
  return Math.min(...path[path.length - 1]);
};

triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]];
console.log(minimumTotal(triangle));
