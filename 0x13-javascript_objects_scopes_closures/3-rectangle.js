#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const x = ''.padStart(this.width, 'X');
    let y = 0;
    while (y < this.height) {
      console.log(x);
      y++;
    }
  }
};
