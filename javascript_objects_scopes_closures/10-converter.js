#!/usr/bin/node
// Converter!
exports.logMe = (function () {
  let count = 0;

  return function (item) {
    console.log(`${count}: ${item}`);
    count++; // Increment the count for the next call
  };
})();

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
