$(document).ready(function () {
  const redHeaderDiv = $('DIV#red_header');

  // Event handler
  redHeaderDiv.click(function () {
    const headerElement = $('header');

    if (headerElement) {
      headerElement.css('color', '#FF0000');
    } else {
      console.error('Header element not found');
    }
  });
});
