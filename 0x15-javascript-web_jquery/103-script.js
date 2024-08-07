$(document).ready(function () {
  // Attach click event to the translate button
  $("INPUT#btn_translate").click(translate);

  // Attach keydown event to the language code input field
  $("INPUT#language_code").on("keydown", function (e) {
    if (e.keyCode === 13) {
      // Enter key
      translate();
    }
  });
});

function translate() {
  const url = "https://www.fourtonfish.com/hellosalut/?";
  $.get(
    url + $.param({ lang: $("INPUT#language_code").val() }),
    function (data) {
      $("DIV#hello").html(data.hello);
    }
  );
}
