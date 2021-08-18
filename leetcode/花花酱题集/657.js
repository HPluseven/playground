/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function (moves) {
  const ori = [0, 0];
  const steps = {
    U: [0, 1],
    R: [1, 0],
    D: [0, -1],
    L: [-1, 0],
  };
  for (const direction of moves) {
    const step = steps[direction];
    ori[0] += step[0];
    ori[1] += step[1];
  }

  return ori[0] === 0 && ori[1] === 0;
};

const moves = "LL";
console.log(judgeCircle(moves));
