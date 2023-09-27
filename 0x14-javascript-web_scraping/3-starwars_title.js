#!/usr/bin/node

// Reads and prints the title of a Star Wars movie based on an episode number
const request = require('request');
const episodeNumber = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${episodeNumber}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error.message);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});

