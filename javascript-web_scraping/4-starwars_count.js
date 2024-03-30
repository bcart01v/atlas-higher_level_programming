#!/usr/bin/node
// Prints number of movies where "Wedge Antilles" is present
const request = require('request');
const apiUrl = process.argv[2];
const wedgeAntillesId = '18'; // Character ID for Wedge Antilles

request(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    return;
  }

  let count = 0;
  body.results.forEach(film => {
    if (film.characters.some(characterUrl => characterUrl.endsWith(`/${wedgeAntillesId}/`))) {
    count++;
    }
  });

  console.log(count);
});
