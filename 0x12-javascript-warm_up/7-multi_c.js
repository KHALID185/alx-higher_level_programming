#!/usr/bin/node
const _x = Math.floor(Number(process.argv[2]));
if (isNaN(_x)) {
  console.log('Missing number of occurrences');
} else {
  for (let j = 0; j < _x; j++) {
    console.log('C is fun');
  }
}
