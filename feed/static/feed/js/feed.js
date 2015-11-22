function loadActivities() {
    $.ajax({
        url: "feed/",
        type: "GET",

        success: function(html) {
            $("#feed").html(html);
            startTimelineAnimation();
            startListeningEvents();
        },
        error: function(xhr, errmsg, err) {
            console.log("failed fetching activities...");
        },
    });
}

function startListeningEvents() {
    $(".expand-activities").click(function() {
        $.ajax({
            url: "feed/raw/",
            type: "GET",

            success: function(html){
                $("#cd-timeline").html(html);
                startTimelineAnimation();
                startListeningEvents();
            },
        });
    });

    $("#submit").click(function() {
        $("#text").val("");
    });

    $(".give-thumbs").click(function() {
        if ($(this).hasClass("fa-thumbs-o-up")) {
            $(this).removeClass("fa-thumbs-o-up").addClass("fa-thumbs-up");
        }
        else {
            $(this).removeClass("fa-thumbs-up").addClass("fa-thumbs-o-up");
        }
    });
}
