#!/usr/bin/node
// Now only prints the first argument.
const FirstArg = process.argv[2];

if (FirstArg === undefined) {
    console.log('No argument');
} else {
    console.log(FirstArg);
}