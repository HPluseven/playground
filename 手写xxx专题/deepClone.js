const isObject = (obj) => obj !== null && typeof obj === "object";

function deepClone(obj, hash = new WeakMap()) {
  if (!isObject(obj)) return obj;
  if (hash.has(obj)) {
    return hash.get(obj);
  }

  const res = Array.isArray(obj) ? [] : {};
  hash.set(obj, res);
  Reflect.ownKeys(obj).forEach((key) => (res[key] = deepClone(obj[key], hash)));
  return res;
}

var obj1 = {
  a: 1,
  b: { a: 2 },
};
var obj2 = deepClone(obj1);
console.log(obj1);
console.log(obj1 === obj2);
