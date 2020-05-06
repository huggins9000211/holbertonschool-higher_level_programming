#!/usr/bin/node
const x = parseInt(process.argv[2]);
let y = 0;
const z = ''.padStart(x, 'x');
if (x) {
  while (y < x) {
    console.log(z);
    y++;
  }
} else {
  console.log('Missing size');
}
