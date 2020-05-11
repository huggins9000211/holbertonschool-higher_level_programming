#!/usr/bin/node
const Square1 = require('./5-square.js');
module.exports = class Square extends Square1 {
  charPrint (c) {
    const x = ''.padStart(this.width, c);
    let y = 0;
    while (y < this.height) {
      console.log(x);
      y++;
    }
  }
};
