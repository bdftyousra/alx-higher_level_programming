#!/usr/bin/node
// Displays the status code of a GET request

const request = require('request');
const argv = process.argv;
let url = argv[2];

request.get(url).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
