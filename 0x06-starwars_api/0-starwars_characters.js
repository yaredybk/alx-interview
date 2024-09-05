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

const baseUrl = 'https://swapi-api.alx-tools.com/api/';
request(`${baseUrl}films/${movieId}/`, (error, response, body) => {
	if (error) {
		console.error('Error:\n', error);
	} else {
		const data = JSON.parse(body);
		char_urls = data.characters
		get_all_name(char_urls, 0);
    }
});

async function get_name(charUrl) {
	return new Promise((resolve, reject) => {
		request(charUrl, (error, response, body) => {
		    if (error) {
			    reject('Error:\n', error);
		    } else {
			    const data = JSON.parse(body);
			    resolve(data.name)
		    }
		});
	})
}

function get_all_name(char_urls, ind) {
	if (char_urls[ind]) {
		get_name(char_urls[ind]).then((name) => {
			console.log(name);
		}).catch((error) => {
			console.warn(`error @INDEX:${ind}`)
		}).finally(() => {
			get_all_name(char_urls, ++ind);
		})
	}
}
