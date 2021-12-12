function inheritObject(o) {
  // if (this instanceof inheritObject) {
  //   console.log('211323123');
  // }

  function F() {}
  F.prototype = o;
  return new F();
}

let book = {
  // constructor: function () {
  //   return 1;
  // },
  name: "hjq",
  alikeBook: ["css book", "html book"],
};

let newBook = inheritObject(book);
// console.log(typeof newBook);
// console.log(newBook.__proto__);
// console.log(newBook.constructor.name);
// newBook.name = 'sas'
// console.log(newBook.name);
// console.log(newBook.__proto__.name);
// newBook.alikeBook = 1
// console.log(newBook.alikeBook);
// console.log(newBook.__proto__.alikeBook);

// let o = new inheritObject(book);
// console.log(o.__proto__);

