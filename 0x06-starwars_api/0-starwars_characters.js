#!/usr/bin/node

const util = require('util'); // util module for utility functions
const request = util.promisify(require('request')); // import req module promisify callback func
const movieID = process.argv[2]; // getting movie id passed as arg

// async function to get the characters
async function starwarsCharacters (movieId) {
 try {
  const endpoint = 'https://swapi-api.hbtn.io/api/films/' + movieId;
  let response = await (await request(endpoint)).body; // making http req and waiting
  response = JSON.parse(response); // parsing json response
  const characters = response.characters; // getting the characters from film

// looping evry characte and getting their info
  for (let c = 0; c < characters.length; c++) {
    const urlCharacter = characters[c]; // url of character info
    let character = await (await request(urlCharacter)).body; // requesting char info
    character = JSON.parse(character);
    console.log(character.name); // displaying char name
  }
} catch (error) {
  console.error('Error fetching Star Wars characters:', error);
  }
}
starwarsCharacters(movieID); // function is called with te movie ID
