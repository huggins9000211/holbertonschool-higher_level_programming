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

  rotate () {
    this.height = [this.width, this.width = this.height][0];
  }

  double () {
    this.width = [this.width * 2, this.height = this.height * 2][0];
  }
};
