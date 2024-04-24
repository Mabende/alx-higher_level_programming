#!/usr/bin/node
const myLetter = process.argv[2];
if(isNaN(myLetter)){console.log('Missing size');}
else{ for(let i = 0; i < myLetter; i++){console.log('X'.repeat(myLetter));}}
