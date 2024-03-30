#!/usr/bin/node
// Get content of webpage and store it in a file.

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Usage: node script.js <URL> <file path to store body response>');
  process.exit(1);
}

request(url, (error, response, body) => {
  fs.writeFile(filePath, body, { encoding: 'utf-8' }, err => {
  });
});
