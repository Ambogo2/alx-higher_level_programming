#!/usr/bin/node

const fs = require('fs');
const srcfile1 = fs.readFileSync(process.argv[2], 'utf8');
const srcfile2 = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], srcfile1 + srcfile2);
