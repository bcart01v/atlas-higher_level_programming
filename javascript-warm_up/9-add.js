#!/usr/bin/node
// Create function, add 2 things.

function add(a,b) {
  return (a + b);
}

const firstVal = process.argv[2];
const secVal = process.argv[3];

const num1 = Number(firstVal);
const num2 = Number(secVal);

console.log(add(num1, num2));
