#!/usr/bin/node
// Compute number of tasks completed by User ID

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, { json: true }, (error, response, todos) => {

  const completedTasksByUser = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (completedTasksByUser.hasOwnProperty(todo.userId)) {
        completedTasksByUser[todo.userId]++;
      } else {
        completedTasksByUser[todo.userId] = 1;
      }
    }
  });

  console.log(completedTasksByUser);
});
