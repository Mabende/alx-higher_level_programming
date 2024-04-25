#!/usr/bin/node
const myArg = process.argv[2];
const myNumber = parseInt(myArg);
console.log(isNaN(myNumber) ? 'Not a number' : 'My number: ' + myNumber);
