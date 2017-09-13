jQuery(document).ready(function ($) {

	$(window).load(function () {
		$(".loaded").fadeOut();
		$(".preloader").delay(1000).fadeOut("slow");
	});
    
    $('#check-me-out').on('click',function(){
        $('html, body').animate({
        scrollTop: $("#about").offset().top
    }, 1000);
    });
    $('#g-btn').on('click',function(){ 
        console.log($('#user-input').val());
        $.get('/get_message/'+ $('#user-input').val()).done(function(data){
            $('#text-field').children().fadeOut(300, function(){ $(this).remove();});
            create_response(data);
        })
    })
    function create_response(text) {
        var div = document.createElement('div');
        $(div).text(text); 
        $('#text-field').append(div).fadeIn(310);
    }

});
