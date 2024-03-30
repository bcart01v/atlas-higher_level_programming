#!/usr/bin/node
// Print title of star wars movie based on episode number

const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieID}`;

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    return;
  }
  console.log(body.title);
});
