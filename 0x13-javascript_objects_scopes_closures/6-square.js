#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends
SquareP {
	charPrint (c) {
		if (c === null) {
			c = 'X';
		}
		for (let i = 0; i < tjis.height; i++) {
			let s = '';
			for (let j = 0; j < this.width; j++) {
				s += c;
			}
			console.log(s);
		}
	}
}
module.exports = Square;
