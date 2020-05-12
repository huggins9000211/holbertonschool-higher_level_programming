#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) console.error('error:', error);
  console.log('statusCode:', response && response.statusCode);
  // console.log('body:', body);
});
