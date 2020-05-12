#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request(process.argv[2], function (error, response, body) {
  if (error) {
    // console.error('error:', error);
  }
  fs.writeFile(process.argv[3], body, (err) => {
    if (err) {
      console.log(err);
    }
  });
});
