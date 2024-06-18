#!/usr/bin/node
const process = require('process');
const msg = 'No argument';
if (process.argv[2] === undefined) {
  console.log(msg);
} else {
  console.log(process.argv[2]);
}
