/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
  let res = 0;
  const m = grid.length;
  const n = grid[0].length;
  const marked = new Array(m);
  for (let i = 0; i < marked.length; i++) {
    marked[i] = new Array(n).fill(false);
  }

  const dfs = (i, j) => {
    if (
      i < 0 ||
      i >= m ||
      j < 0 ||
      j >= n ||
      grid[i][j] === "0" ||
      marked[i][j] === true
    ) {
      return;
    }
    marked[i][j] = true;
    dfs(i + 1, j);
    dfs(i - 1, j);
    dfs(i, j + 1);
    dfs(i, j - 1);
  };

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (!marked[i][j] && grid[i][j] === "1") {
        res++;
        dfs(i, j);
      }
    }
  }
  return res;
};

const grid =[
  ["1","1","0","0","0"]
]


console.log(numIslands(grid));
