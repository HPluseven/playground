/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  const str = s.replace(' ', '')
  const arr = Array.from(str)
  const stack = []
  while (arr.length > 0) {
    const char = arr.shift()
    if (char === '(' || char === '[' || char === '{') {
      stack.push(char)
    } else if (char === ')' || char === ']' || char === '}') {
      const temp = stack.pop()
      if (temp === '(' && char === ')') continue
      if (temp === '[' && char === ']') continue
      if (temp === '{' && char === '}') continue
      return false
    }
  }
  if (stack.length === 0) return true
  return false
};


const questions = ["()", "()[]{}", "(]", "([)]", "{[]}", "  { ]", "]"]
const answers = [true, true, false, false, true]
const result = []

questions.forEach(value => {
  result.push(isValid(value))
})
console.log(result);

// const str = "()[]{}"
// console.log(isValid(str));