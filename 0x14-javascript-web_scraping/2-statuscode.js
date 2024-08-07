#!/usr/bin/node

// Import the module
const request = require('request');

const url = process.argv[2];

// Make an HTTP GET request to the specified URL
request(url, function (error, response, body) {
  // Check for errors during the request
  if (error) {
    console.error(error);
  } else {
    // If there are no errors, print the HTTP status code
    console.log('code:', response.statusCode);
  }
});
