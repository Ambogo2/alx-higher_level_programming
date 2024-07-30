#!/usr/bin/node

// Import the module
const request = require('request');

// The first argument is the API URL
const apiUrl = process.argv[2];

// Make an HTTP GET request to the API
request(apiUrl, function (error, response, body) {
  if (!error) {
    // Parse the JSON response
    const results = JSON.parse(body).results;

    // Count number of movies where "Wedge Antilles" is present
    const moviesWithWedge = results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1 // If found
        : count; // If not found
    }, 0); // Initializing count to zero
    console.log(moviesWithWedge);
  }
});
