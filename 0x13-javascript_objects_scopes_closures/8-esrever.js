#!/usr/bin/node
exports.esrever = function (list) {
  const result = [];
  for (let x = list.length - 1; x >= 0; x++) {
    result.push(list[x]);
  }
  return result;
};
