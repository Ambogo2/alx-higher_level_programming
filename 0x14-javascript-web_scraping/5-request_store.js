#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const apiUrl = process.argv[2];
const filepath = process.argv[3];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filepath, body, 'utf8', function (error, data) {
      if (error) {
        console.error(error);
      }
    });
  }
});
