$(document).ready(function () {
    const element = $('header');

    if (element) {
      element.style.color = '#FF0000';
    } else {
      console.error('Header element not found');
    }
});
