#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function helpRequest (arr, i) {
  if (i === arr.length) {
    return;
  }
  request(arr[i], function (error, response, body) {
    if (error) {
      console.log(error);
    }
    console.log(JSON.parse(body).name);
    helpRequest(arr, i + 1);
  });
}

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const charac = JSON.parse(body).characters;
  helpRequest(charac, 0);
});
