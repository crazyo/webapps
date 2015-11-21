$(document).ready(function() {
    setInterval(function() {
        $.ajax({
            url: 'chat/',
            type: 'GET',

            success: function(html) {
                $('#messages').html(html);
            },
            error: function() {
            },
        });
    }, 1000);

    $('#submit').click(function() {
        console.log($('#input').val());
        $.ajax({
            beforeSend: function(xhr, settings) {
                // add csrf token to header
                setHeaderCsrf(xhr, settings);
            },

            url: 'chat/',
            type: 'POST',
            data: {text: $('#input').val()},

            success: function() {
                $('#input').val('');
            },
            error: function(xhr, errmsg, err) {
            }
        });
    });

    var open = false;
    $('#chat-trigger-wrapper').click(function() {
        if (open) {
            $("#chat-wrapper").animate({height: 0});
            $("#chat-trigger-wrapper").animate({bottom: "20px"});
            open = false;
        } else {
            $("#chat-wrapper").animate({height: "500px"});
            $("#chat-trigger-wrapper").animate({bottom: "550px"});
            open = true;
        }
    });
});
