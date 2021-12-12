// let Book = function (id, name, price) {
//   let num = 1;
//   function checkId() {
//     console.log('asasdasd');
//   }
//   this.getName = function () {
//     checkId()
//   };
//   this.getNum = function () {
//     return num;
//   };
//   this.setNum = function (newNum) {
//     num = newNum;
//   };
// };

// b1 = new Book(1, "js", 2);
// b1.setNum(2);
// console.log(b1.getNum());
// b2 = new Book(2, "java", 2);
// console.log(b2.getNum());
// b1.getName()

// let Book = (function () {
//   let bookNum = 0;
//   function checkBook(name) {}
//   return function (newId, newName, newPrice) {
//     let name, price;
//     function checkId() {}
//     this.setBookNum = function (num) {
//       bookNum = num;
//     };
//     this.getBookNum = function () {
//       return bookNum;
//     };
//   };
// })();
// Book.prototype = {
//   isJsBook: 121,
//   display: function () {},
// };

// book = new Book();
// book2 = new Book();
// book.setBookNum(13123);
// console.log(book2.getBookNum());
// console.log(new Book().isJsBook);
// console.log(book.bookNum);

let Book = (function () {
  let bookNum = 0;
  function checkBook(name) {}
  function _book(newId, newName, newPrice) {
    let name, price;
    function checkId() {}
    this.setBookNum = function (num) {
      bookNum = num;
    };
    this.getBookNum = function () {
      return bookNum;
    };
  }
  _book.prototype = {
    isJsBook: 121,
    display: function () {},
  };
  return _book;
})();
b1 = new Book(1, 1, 1);
console.log(b1.isJsBook);
