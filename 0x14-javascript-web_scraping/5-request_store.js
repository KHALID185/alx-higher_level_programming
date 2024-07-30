#!/usr/bin/node
// script to get the content of a page and store it

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(file, body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
