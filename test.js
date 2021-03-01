var value = 1;

function foo() {
  console.log(value);
}

function bar() {
  var value = 2;
  foo();
}

bar();

/**
 *
 * @param {Object} obj
 */
function deepClone(obj = {}) {
  if (typeof obj !== "object" || obj == null) {
    return obj;
  }

  let result;
  if (obj instanceof Array) {
    result = [];
  } else {
    result = {};
  }

  for (const key in obj) {
    if (Object.hasOwnProperty.call(obj, key)) {
      result[key] = deepClone(obj[key]);
    }
  }
  return obj;
}

Function.prototype.bind = function () {
  const args = new Array.from(arguments);
  const t = args.unshift();
  const self = this;
  return function () {
    return self.apply(t, args);
  };
};



