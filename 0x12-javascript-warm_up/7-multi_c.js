#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (!num) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= num; i++) {
    console.log('C is fun');
  }
}
