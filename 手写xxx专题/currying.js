function currying(fn, ...args) {
  if (fn.length <= args.length) return fn(...args);
  return (...args2) => currying(fn, ...args, ...args2);
}

const fun = (a, b, c) => console.log(a, b, c);

const curryingFun = currying(fun);
curryingFun(1)(2)(3); // 1 2 3
curryingFun(1, 2)(3); // 1 2 3
curryingFun(1, 2, 3); // 1 2 3
