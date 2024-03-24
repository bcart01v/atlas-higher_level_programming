#!/usr/bin/node
// This script searches for the second biggest integer in the list of arguments.

function findSecondBiggest(args) {
if (args.length < 2) {
  return 0;
}

let firstMax = Number.MIN_SAFE_INTEGER;
let secondMax = Number.MIN_SAFE_INTEGER;

for (const value of args) {
  const num = Number(value);

  if (num > firstMax) {
    secondMax = firstMax;
    firstMax = num;
  } else if (num > secondMax && num < firstMax) {
    secondMax = num;
  }
}

return secondMax;
}

const args = process.argv.slice(2);

console.log(findSecondBiggest(args));
