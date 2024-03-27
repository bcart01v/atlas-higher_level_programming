#!/usr/bin/node
// Log it!
exports.logMe = (function () {
  let counter = 0;

  return function (item) {
    console.log(`${counter}: ${item}`);
    counter++; // Increment the counter after printing
  };
})();
