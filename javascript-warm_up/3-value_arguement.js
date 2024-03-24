#!/usr/bin/node
// Figures the number of arguments passed, and prints output based on argument count.
const args = process.argv.slice(2); 
// This would print the first argument, but if more is passed nothing will happen.
// Don't know if that's in the scope, we'll see.
if (args.length === 0) {
    console.log('No argument');
} else if (args.length === 1) {
    console.log(args);
}
