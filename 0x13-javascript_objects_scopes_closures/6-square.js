#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    const x = ''.padStart(this.width, c);
    let y = 0;
    while (y < this.height) {
      console.log(x);
      y++;
    }
  }
};
