#!/usr/bin/node
// Read and print content of file.
const fs = require('fs');
const path = process.argv[2];

fs.readFile(path, { encoding: 'utf-8' }, (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
