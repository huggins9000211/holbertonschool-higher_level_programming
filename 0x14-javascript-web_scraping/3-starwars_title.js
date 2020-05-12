#!/usr/bin/node
const request = require('request');

request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, function (error, response, body) {
  if (error) console.error('error:', error);
  // console.log('code:', response && response.statusCode);
  console.log(JSON.parse(body).title);
});
