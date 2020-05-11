#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (var x in list) {
    if (x === searchElement) {
      count++;
    }
  }
  return count;
};
