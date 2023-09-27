#!/usr/bin/node
// Prints the number of movies where "Wedge Antilles" is present

const request = require('request');
const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    let films = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < films.length; i++) {
      for (let j = 0; j < films[i].characters.length; j++) {
        if (films[i].characters[j].includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('Invalid');
  }
});
