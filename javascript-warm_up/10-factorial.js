#!/usr/bin/node
// This script prints the factorial of what the user passed.

function factorial(n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const arg = process.argv[2];
const num = parseInt(arg, 10);

console.log(factorial(num));
