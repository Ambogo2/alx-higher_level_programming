#!/usr/bin/node

if (process.argv.length === 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  console.log(`${parseInt(process.argv[2])}`);
}
