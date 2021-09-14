class Promise {
  succeed = null;
  fail = null;
  state = "pending";

  constructor(fn) {
    fn(this.resolve.bind(this), this.reject.bind(this));
  }

  resolve(result) {
    setTimeout(() => {
      this.state = "fulfilled";
      this.succeed(result);
    });
  }

  reject(reason) {
    setTimeout(() => {
      this.state = "rejected";
      this.fail(reason);
    });
  }

  then(succeed, fail) {
    this.succeed = succeed;
    this.fail = fail;
  }
}

Promise.all = function (arrP) {
  const list = [];
  let hasReject = false;
  let cnt = 0;

  return new Promise((resolve, reject) => {
    for (const P of arrP) {
      P.then((data) => {
        list.push(data);
        cnt++;
        list.length === cnt && resolve(list);
      }).catch((err) => {
        !hasReject && reject(err);
        hasReject = true;
      });
    }
  });
};
