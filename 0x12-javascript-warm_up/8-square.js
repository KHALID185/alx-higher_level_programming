#!/usr/bin/node
const sz = Math.floor(Number(process.argv[2]));
if (isNaN(sz)) {
  console.log('Missing size');
} else {
  for (let r = 0; r < sz; r++) {
    let row = '';
    for (let c = 0; c < sz; c++) row += 'X';
    console.log(row);
  }
}
