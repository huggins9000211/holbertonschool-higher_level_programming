#!/usr/bin/node
const Square1 = require('./5-square.js');
module.exports = class Square extends Square1 {
  charPrint (c = 'X') {
    let y = 0;
    while (y < this.height) {
      console.log(c);
      y++;
    }
  }
};
