// Script to change text from red to green
$(document).ready(function() {
    $('#toggle_header').click(function() {
        if($('header').hasClass('red')) {
            $('header').removeClass('red').addClass('green');
        } else {
            $('header').removeClass('green').addClass('red');
        }
    });
});