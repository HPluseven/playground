/**
 * @param {number[][]} grid
 * @return {number}
 */
var islandPerimeter = function (grid) {
  const row = grid.length;
  const col = grid[0].length;
  let perimeter = 0;

  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      if (grid[i][j] === 1) {
        if (i - 1 < 0 || grid[i - 1][j] === 0) perimeter++;
        if (i + 1 >= row || grid[i + 1][j] === 0) perimeter++;
        if (j - 1 < 0 || grid[i][j - 1] === 0) perimeter++;
        if (j + 1 >= col || grid[i][j + 1] === 0) perimeter++;
      }
    }
  }

  return perimeter;
};
