#!/usr/bin/node
/*
 * Write a script that prints all characters of a Star Wars movie
 */

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const charactersList = JSON.parse(body).results[id].characters;
  for (let i = 0; i < charactersList.length; i++) {
    const characterUrl = charactersList[i];
    request(characterUrl, (err, resp, bio) => {
      if (err) {
        console.log(err);
      }
      console.log(JSON.parse(bio).name);
    });
  }
});
