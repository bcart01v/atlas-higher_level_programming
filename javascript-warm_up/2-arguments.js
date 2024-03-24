#!/usr/bin/node
// Figures the number of arguments passed, and prints output based on argument count.
const args = process.argv.slice(2); 

if (args.length === 0) {
    console.log("No argument");
} else if (args.length === 1) {
    console.log("Argument found");
} else {
    console.log("Arguments found");
}
