#!/usr/bin/node
const num1 = parseInt(process.argv[2]);
function add (a) {
  if (a >= 1) {
    return (a * add(a - 1));
  }
  return 1;
}
console.log(add(num1));
