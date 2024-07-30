#!/usr/bin/node

// Import module
const request = require("request");

const apiUrl = "https://swapi-api.alx-tools.com/api/films/";

// Function to fetch films and count appearances of a specific character
function countMoviesWithCharacter(apiUrl, characterId) {
  request(apiUrl, function (error, response, body) {
    if (error) {
      console.error("Error:", error);
      return;
    }

    try {
      const films = JSON.parse(body).results;
      let count = 0;

      films.forEach((film) => {
        // Check if the characterId is in the film's characters list
        const characterUrls = film.characters;
        characterUrls.forEach((url) => {
          if (url.includes(characterId)) {
            count++;
          }
        });
      });

      console.log(count);
    } catch (parseError) {
      console.error("Error parsing JSON:", parseError);
    }
  });
}

// Character ID for Wedge Antilles
const characterId = "18";

// Count and print the number of movies featuring Wedge Antilles
countMoviesWithCharacter(apiUrl, characterId);
