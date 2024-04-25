#!/usr/bin/node
const myArg = process.argv.slice(2);
let overallMax = 0;
if(myArg.length > 1){
	const integers = myArg.map(Number);
	integers.sort((a, b) => b - a);
	overallMax = integers[1];
}
console.log(overallMax);
