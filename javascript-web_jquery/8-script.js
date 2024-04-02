// Fetch movie names
$(document).ready(function() {
  $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
    $.each(data.results, function(index, movie) {
      $('#list_movies').append($('<li>').text(movie.title));
    });
  });
});
