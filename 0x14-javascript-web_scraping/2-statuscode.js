#!/usr/bin/node

// Import module
const request = require("request");

const url = process.argv[2];

// Make an HTTP GET request to the URL
request(url, function (error, response, body) {
  if (error) {
    console.error("Error:", error);
  } else {
    console.log("Code:", response.statusCode);
  }
});
