$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function () {
}).done(function (data) {
  $('DIV#hello').html(`${data.hello}`);
});
