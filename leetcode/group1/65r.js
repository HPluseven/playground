/**
 * @param {string} s
 * @return {boolean}
 */
var isNumber = function (s) {
  let state = 0;
  const transfer = [
    [0, 1, 3, 2, -1, -1],
    [-1, -1, 3, 2, -1, -1],
    [-1, -1, 4, 2, 5, -1],
    [-1, -1, -1, 4, -1, -1],
    [-1, -1, -1, 4, 5, -1],
    [-1, 6, -1, 7, -1, -1],
    [-1, -1, -1, 7, -1, -1],
    [8, -1, -1, 7, -1, -1],
    [8, -1, -1, -1, -1, -1],
  ];
  const finals = [false, false, true, false, true, false, false, true, true];

  const make = (c) => {
    c = c.toLowerCase();
    switch (c) {
      case " ":
        return 0;
      case "+":
      case "-":
        return 1;
      case ".":
        return 2;
      case "e":
        return 4;
      default:
        let code = c.charCodeAt();
        if (code >= 48 && code <= 57) return 3;
        else return 5;
    }
  };

  for (const c of s) {
    state = transfer[state][make(c)];
    if (state < 0) return false;
  }
  return finals[state];
};

console.log(isNumber("3."));
