$(document).ready(function() {
    setInterval(function() {
        $.ajax({
            url: 'chat/',
            type: 'GET',

            success: function(html) {
                $('#messages').html(html);
            },
            error: function() {
                alert('error!');
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
                console.log(err);
                alert('error');
            }
        });
    });
});
