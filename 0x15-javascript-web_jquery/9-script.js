$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  method: 'GET',
  datatype: 'json',
  success: function (data) {
    // extract character from fetched data
    const translation = data.hello;

    // display the transalation in the div
    $('DIV#hello').text(translation);
  },
});
