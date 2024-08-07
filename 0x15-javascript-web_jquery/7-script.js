// Script to fetch the name of the character of the url

const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('#character').append(data.name);
});
