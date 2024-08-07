$.ajax({
    url: 'https://swapi.dev/api/people/5/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function(data) {
        // Extract character name from fetched data
        const characterName = data.name;

        // Get the <ul> element
        const listElement = $('UL#list_movies');

        // Create and append the list item
        const listItem = $('<li>' + characterName + '</li>');
        listElement.append(listItem);
    },
    error: function(error) {
        console.error('Error fetching data:', error);
    }
});
