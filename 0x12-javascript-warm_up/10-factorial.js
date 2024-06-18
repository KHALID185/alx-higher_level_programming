#!/usr/bin/node
const myArgmt = process.argv.slice(2);
function factorial (num) {
  if (isNaN(myArgmt[0])) {
    return 1;
  }
  if (num <= 1) {
    return 1;
  }
  return num * factorial(num - 1);
}
console.log(factorial(parseInt(myArgmt[0])));
