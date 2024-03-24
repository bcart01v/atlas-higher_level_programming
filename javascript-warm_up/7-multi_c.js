#!/usr/bin/node
// Take the number, print a loop that many time.

const argument = process.argv[2];
number = Number(argument);

if (isNaN(number) || number <= 0) {
  console.log('Missing number of occurrences');
} else {
  const PrintText = 'C is fun';
  for (let i = 0; i < number; i++) {
  console.log(PrintText);
  }
}
