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
            },
        });
    });
}
