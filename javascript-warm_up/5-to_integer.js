#!/usr/bin/node
// Prints the number if it's a number, message if not.
const argument = process.argv[2];

const number = Number(argument);

if (isNaN(number)) {
    console.log('Not a number')
} else {
    console.log(Math.trunc(number))
}