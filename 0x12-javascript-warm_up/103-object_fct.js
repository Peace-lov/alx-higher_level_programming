#!/usr/bin/node
const myObject = {
	type: 'object',
	value: 12
};
console.log(myObject);
myObject.iner = function () {
	this.value++;
};
myObject.iner();
console.log(myObject);
myObject.iner();
console.log(myObject);
myObject.iner();
console.log(myObject);
