$(function(){
    debugger;
    $(".email").click(function(){
        var email = $('.email').val();
        var pattern = "^[a-zA-Z0-9]+@gmail\.com"
        if (pattern.match(email)){
            alert('invalid');
        }
    });

});