#!/usr/bin/node
/**
 * Print all characters of a Star Wars movie.
 *
 * The first positional argument passed is the Movie ID
 * 	example: 3 = “Return of the Jedi”
 * Display one character name per line in the same order as
 * the “characters” list in the /films/ endpoint
 * use the Star wars API
 * use the request module
 */
const request = require('request');

if (process.argv.length < 3){
	throw('Usage: ./0-starwars_characters.js <Movie ID>');
}

const movieId = Number(process.argv[2]);

if (isNaN(movieId)) {
	throw('<Movie ID> must be number');
}

console.log({movieId});
const baseUrl = 'https://swapi-api.alx-tools.com/api/';

request(`${baseUrl}films/${movieId}/`, (error, response, body) => {
    if (error) {
        console.error('Error:\n', error);
    } else {
        console.log('Body:\n', body);
    }
});
