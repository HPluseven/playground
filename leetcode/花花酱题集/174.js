// /**
//  * @param {number[][]} dungeon
//  * @return {number}
//  */
// var calculateMinimumHP = function (dungeon) {
//   const m = dungeon.length;
//   const n = dungeon[0].length;
//   const minHps = new Array(m);
//   for (let i = 0; i < m; i++) {
//     minHps[i] = new Array(n);
//   }

//   const getMin = (x, y) => {
//     if (x[1] === y[1]) {
//       return x[0] >= y[0] ? x : y;
//     } else {
//       return x[1] < y[1] ? x : y;
//     }
//   };

//   for (let i = m - 1; i >= 0; i--) {
//     for (let j = n - 1; j >= 0; j--) {
//       const current = dungeon[i][j];
//       if (i === 0 && j === 0) {
//         minHps[i][j] = [current, 1 - current];
//         continue;
//       }
//     }
//   }
//   // for (let i = 0; i < m; i++) {
//   //   for (let j = 0; j < n; j++) {
//   //     const current = dungeon[i][j];
//   //     if (i === 0 && j === 0) {
//   //       minHps[i][j] = [current, 1 - current];
//   //       continue;
//   //     }
//   //     const left = j > 0 ? minHps[i][j - 1] : [-Infinity, Infinity];
//   //     const up = i > 0 ? minHps[i - 1][j] : [-Infinity, Infinity];
//   //     const min = getMin(left, up);
//   //     minHps[i][j] = [current + min[0], Math.max(min[1], 1 - current - min[0])];
//   //   }
//   // }
//   console.log(minHps);
//   return Math.max(minHps[m - 1][n - 1][1], 1);
// };

/**
 * @param {number[][]} dungeon
 * @return {number}
 */
var calculateMinimumHP = function (dungeon) {
  const m = dungeon.length;
  const n = dungeon[0].length;
  const minHps = new Array(m + 1);
  for (let i = 0; i < m + 1; i++) {
    minHps[i] = new Array(n + 1).fill(Infinity);
  }
  minHps[m][n - 1] = 1;
  minHps[m - 1][n] = 1;

  for (let i = m - 1; i >= 0; i--) {
    for (let j = n - 1; j >= 0; j--) {
      const minn = Math.min(minHps[i + 1][j], minHps[i][j + 1]);
      minHps[i][j] = Math.max(minn - dungeon[i][j], 1);
    }
  }
  return minHps[0][0];
};

const dungeon = [
  [1, -3, 3],
  [0, -2, 0],
  [-3, -3, -3],
];

console.log(calculateMinimumHP(dungeon));
