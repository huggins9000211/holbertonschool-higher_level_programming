#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  const inputS = process.argv.slice(2);
  inputS.sort(function (a, b) { return a - b; });
  console.log(inputS[inputS.length - 2]);
}
