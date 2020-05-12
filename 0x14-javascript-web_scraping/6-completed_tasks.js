#!/usr/bin/node
const request = require('request');
const results = {};
request(process.argv[2], function (error, response, body) {
  if (error) {
    // console.error('error:', error);
  }
  let x;
  for (x of JSON.parse(body)) {
    if (x.completed) {
      const currentId = x.userId;
      if (currentId in results) {
        results[currentId]++;
      } else {
        results[currentId] = 1;
      }
    }
  }
  console.log(results);
});
