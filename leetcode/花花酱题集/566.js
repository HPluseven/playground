/**
 * @param {number[][]} mat
 * @param {number} r
 * @param {number} c
 * @return {number[][]}
 */
// var matrixReshape = function (mat, r, c) {
//   const m = mat.length;
//   const n = mat[0].length;
//   console.log(m, n);
//   const ans = new Array(r);

//   for (let i = 0; i < r; i++) {
//     ans[i] = new Array(c);
//   }

//   if (m * n !== r * c) {
//     return mat;
//   }

//   for (let i = 0; i < m; i++) {
//     for (let j = 0; j < n; j++) {
//       const x = Math.floor((i * n + j) / c);
//       const y = (i * n + j) % c;
//       console.log(x, y);
//       ans[x][y] = mat[i][j];
//     }
//   }
//   return ans;
// };
var matrixReshape = function (mat, r, c) {
  const m = mat.length;
  const n = mat[0].length;

  if (m * n !== r * c) {
    return mat;
  }

  const ans = new Array(r).fill(0).map(() => new Array(c).fill(0));

  for (let i = 0; i < m * n; i++) {
    ans[Math.floor(i / c)][i % c] = mat[Math.floor(i / n)][i % n];
  }
  return ans;
};
const mat = [[1], [2], [3], [4]];
const r = 2;
const c = 2;
console.log(matrixReshape(mat, r, c));
