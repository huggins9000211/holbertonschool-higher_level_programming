#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  var x;
  for (x of list) {
    if (x === searchElement) {
      count++;
    }
  }
  return count;
};
