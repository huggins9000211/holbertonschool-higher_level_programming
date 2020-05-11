#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let x;
  for (x of list) {
    if (x === searchElement) {
      count++;
    }
  }
  return count;
};
