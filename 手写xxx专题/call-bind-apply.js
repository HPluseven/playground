Function.prototype.myCall = (context, ...args) => {
  if (!context || context === null) {
    context = window;
  }

  const fn = Symbol();
  context[fn] = this;
  return context[fn](...args);
};

Function.prototype.myApply = (context, args) => {
  if (!context || context === null) {
    context = window;
  }

  const fn = Symbol();
  context[fn] = this;
  return context[fn](...args);
};

Function.prototype.myBind = (context, ...args) => {
  if (!context || context === null) {
    context = window;
  }
  const fn = Symbol();
  context[fn] = this;
  const _this = this;

  const result = function (...innerArgs) {
    if (this instanceof _this) {
      this[fn] = _this;
      this[fn](...[...args, ...innerArgs]);
      delete this[fn];
    } else {
      context[fn](...[...args, ...innerArgs]);
      delete this[fn];
    }
  };

  result.prototype = Object.create(this.prototype);
  return result;
};
