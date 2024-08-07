$(document).ready(function () {
  const toggleDiv = $('DIV#toggle_header');
  const headerElement = $('header')

  // click Event handler
  toggleDiv.click(function () {
     headerElement.toggleClass('red green');
  });
});
