$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  method: 'GET',
  datatype: 'json',
  success: function(data) {
    // extract character from fetched data
    const charName = data.name;

    // display the charater name in the div
    $('DIV#character').text(charName);
  }
});
