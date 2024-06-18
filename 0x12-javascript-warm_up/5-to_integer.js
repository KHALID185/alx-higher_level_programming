#!/usr/bin/node
const _num = Math.floor(Number(process.argv[2]));
console.log(isNaN(_num) ? 'Not a number' : `My number: ${_num}`);
