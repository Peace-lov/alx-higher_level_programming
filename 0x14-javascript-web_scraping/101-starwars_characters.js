#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
let characters = [];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

    const content = JSON.parse(body);
    characters = content.characters;
    getCharacters(0);
 });

    const getCharacters = (index) => {
         if (index === characters.length) {
            return;
         }

request(characters[index], (error, response, body) => {
        if (error) {
          console.log(error);
          return;
        }
          const characternames = JSON.parse(body);
          console.log(characternames.name);
          getCharacters(index + 1);
        });
};
