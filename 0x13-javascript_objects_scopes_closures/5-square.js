#!/usr/bin/node

// the path to the interpreter for the script.

const Rectangle = require('./4-rectangle');
// Import the Rectangle class

class Square extends Rectangle {
	constructor (size) {
// This is the constructor of the Square
// It initializes the Square with the given size
		super(size, size);
	}
}

module.exports = Square;
// Export the Square class
