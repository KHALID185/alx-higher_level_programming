#!/usr/bin/node
const process = require('process');
let msg;
if (process.argv.length === 3) {
  msg = 'Argument found';
} else if (process.argv.length < 3) {
  msg = 'No argument';
} else {
  msg = 'Arguments found';
}
console.log(msg);
