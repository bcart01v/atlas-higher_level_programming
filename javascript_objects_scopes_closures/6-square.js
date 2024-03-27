#!/usr/bin/node
// Square with extension

const Square = require('./5-square');

class CustomSquare extends Square {
  constructor(size) {
    super(size);
  }

  charPrint(c) {
    const char = c !== undefined ? c : 'X';

    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}
module.exports = CustomSquare;
