$(document).ready(function () {
  // Event handler for adding a new item to the list
  $("DIV#add_item").click(function () {
    $("UL.my_list").append("<li>Item</li>");
  });

  // Event handler for removing the last item from the list
  $("DIV#remove_item").click(function () {
    $("UL.my_list li:last").remove();
  });

  // Event handler for clearing all items from the list
  $("DIV#clear_list").click(function () {
    $("UL.my_list").empty();
  });
});
