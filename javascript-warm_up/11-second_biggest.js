#!/usr/bin/node

const number = process.argv.slice(2);

if (process.argv.length < 4) {
  console.log('0');
} else {
  number.sort((a, b) => b - a);
  console.log(number[1]);
}
