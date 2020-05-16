$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function () {
}).done(function (data) {
  $(function () {
    $('DIV#character').html(data.name);
  });
});
