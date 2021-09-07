/**
 * @param {string} expression
 * @return {number[]}
 */
var diffWaysToCompute = function (expression) {
  const memory = new Map();

  const divide = (expression) => {
    if (!isNaN(expression)) return [parseInt(expression)];

    if (memory.has(expression)) return memory.get(expression);

    const res = [];
    for (let i = 0; i < expression.length; i++) {
      const char = expression[i];
      if (["+", "-", "*"].includes(char)) {
        const leftExpression = expression.slice(0, i);
        const rightExpression = expression.slice(i + 1);
        const left = diffWaysToCompute(leftExpression);
        const right = diffWaysToCompute(rightExpression);

        if (!memory.has(leftExpression)) memory.set(leftExpression, left);
        if (!memory.has(rightExpression)) memory.set(rightExpression, right);

        for (const l of left) {
          for (const r of right) {
            if (char === "+") {
              res.push(l + r);
            } else if (char === "-") {
              res.push(l - r);
            } else if (char === "*") {
              res.push(l * r);
            }
          }
        }
      }
    }
    return res;
  };

  return divide(expression);
};

const expression = "10+5";
console.log(diffWaysToCompute(expression));
