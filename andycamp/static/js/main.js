window.onload = Loaded;

function Loaded(){ document.getElementById("loading").style.display="none"; }

$(document).on('ready',function(){
   function Adjust(){
        var hwindow = 300;
        if(!jQuery.browser.mobile) {
            if (window.innerHeight){ hwindow = window.innerHeight - 50;}
            else{ hwindow = document.documentElement.clientHeight - 50;}
        }


        $('.sl-slider-wrapper, .sl-slide, .sl-slides-wrapper, .sl-slide-inner').css('height',hwindow);
    }
    Adjust();
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if(settings.type == "POST"){
                xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
            }
        }
    });
    $('#send').click(function(e){
        e.preventDefault();
        data = {
            name: $('#name').val(),
            email: $('#email').val(),
            message: $('#message').val()
        }
        $.post('send/mail/',data,
        function(a){
                /*TODO: cambiar esta alerta por un bonito mensaje*/
            alert(a);
            $('#email').val('');$('#message').val('');$('#name').val('');
        });
    });
   AndyCampLocation();
   $( window ).resize(function() { Adjust(); });
   $('.navbar-brand').focus();
});



