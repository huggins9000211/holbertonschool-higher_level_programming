#!/usr/bin/node
const x = parseInt(process.argv[2]);
let y = 0;
if (x) {
  while (y < x) {
    console.log('C is fun');
    y++;
  }
} else {
  console.log('Missing number of occurrences');
}
