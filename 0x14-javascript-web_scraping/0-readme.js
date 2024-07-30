#!/usr/bin/node

// import module
const fs = require('fs');

const filepath = process.argv[2];

// read the file
fs.readFile(filepath, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
    return;
  }

  console.log(data);
});
