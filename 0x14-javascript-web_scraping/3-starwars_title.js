#!/usr/bin/node

// Import module
const request = require('request');

const movieId = process.argv[2];

const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

// making HTTP GET request to the API
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
