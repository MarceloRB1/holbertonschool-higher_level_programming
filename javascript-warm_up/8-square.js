#!/usr/bin/node

const times = process.argv[2];

if (isNaN(times) === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < times; i++) {
    console.log('X'.repeat(times));
  }
}
