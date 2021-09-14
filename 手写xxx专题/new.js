function myNew(fn, ...args) {
  let obj = Object.create(fn.prototype);
  const res = fn.apply(obj, args);
  if (res && (typeof res === "object" || typeof res === "object")) {
    return res;
  }

  return obj;
}
