#!/usr/bin/node
// This function prints a square.

const size = process.argv[2];

const num = Number(size);
if (isNaN(num)) {
  console.log('Missing size')
} else {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
}