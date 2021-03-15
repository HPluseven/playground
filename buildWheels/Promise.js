



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
