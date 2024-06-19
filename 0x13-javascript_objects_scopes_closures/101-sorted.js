#!/usr/bin/node

// This line specifies the path

const dict = require('./101-data').dict;
// Import the "dict" object

const totalist = Object.entries(dict);
// Convert the "dict" object into an array

const vals = Object.values(dict);
// Get an array of all the values

const valsUniq = [...new Set(vals)];
// Remove duplicate value

const newDict = {};
// Initialize an empty object

for (const j in valsUniq) {
	// Iterate through each unique value.

	const list = [];
	// Initialize an empty list to store keys

	for (const k in totalist) {
		if (totalist[k][1] === valsUniq[j]) {
			list.unshift(totalist[k][0]);
		}
	}

	newDict[valsUniq[j]] = list;

console.log(newDict);
