#!/usr/bin/node

function fact (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}

if (!isNaN(parseInt(process.argv[2]))) {
  console.log(fact(parseInt(process.argv[2])));
} else {
  console.log('1');
}
