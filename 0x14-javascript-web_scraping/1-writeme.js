#!/usr/bin/node

// import module
const fs = require('fs');

const filepath = process.argv[2];

const content = process.argv[3];

// read the file
fs.writeFile(filepath, content, 'utf8', err => {
  if (err) {
    console.error('Error writing file:', err);
  }
});
