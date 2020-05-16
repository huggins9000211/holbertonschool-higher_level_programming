$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function () {
}).done(function (data) {
  let x;
  const titles = [];
  console.log(data.results);
  for (x of data.results) {
    console.log(x.title);
    titles.push(x.title);
  }
  for (x of titles) {
    console.log(x);
    $('UL#list_movies').append(`<li>${x}</li>`);
  }
});
