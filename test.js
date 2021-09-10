// var value = 1;

// function foo() {
//   console.log(value);
// }

// function bar() {
//   var value = 2;
//   foo();
// }

// bar();

// /**
//  *
//  * @param {Object} obj
//  */
// function deepClone(obj = {}) {
//   if (typeof obj !== "object" || obj == null) {
//     return obj;
//   }

//   let result;
//   if (obj instanceof Array) {
//     result = [];
//   } else {
//     result = {};
//   }

//   for (const key in obj) {
//     if (Object.hasOwnProperty.call(obj, key)) {
//       result[key] = deepClone(obj[key]);
//     }
//   }
//   return obj;
// }

// Function.prototype.bind = function () {
//   const args = new Array.from(arguments);
//   const t = args.unshift();
//   const self = this;
//   return function () {
//     return self.apply(t, args);
//   };
// };

// Function.prototype.bind = function () {
//   const args = Array.from(arguments);
//   const t = args.unshift();
//   const self = this;
//   return function () {
//     self.apply(t, args);
//   };
// };

function flatter(arr) {
  return arr.reduce(
    (pre, cur) =>
      Array.isArray(cur) ? pre.concat(flatter(cur)) : pre.concat(cur),
    []
  );
}

var arr1 = [1, 2, 3, [1, 2, 3, 4, [2, 3, 4]]];
console.log(flatter(arr1));
