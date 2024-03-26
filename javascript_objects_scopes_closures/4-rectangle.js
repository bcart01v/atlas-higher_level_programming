#!/usr/bin/node
// Print, rotate, or double the rectangle.

class Rectangle {
  constructor(w, h) {
  if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }
  }

  print() {
    if (this.width && this.height) {
      for (let row = 0; row < this.height; row++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  rotate() {
    if (this.width && this.height) {
      const temp = this.width;
      this.width = this.height;
      this.height = temp;
    }
  }

  double() {
    if (this.width && this.height) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

module.exports = Rectangle;
