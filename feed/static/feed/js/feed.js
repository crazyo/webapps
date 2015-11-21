function loadActivities() {
    $.ajax({
        url: "feed/",
        type: "GET",

        success: function(html) {
            $("#feed").html(html);
            startTimelineAnimation();
        },
        error: function(xhr, errmsg, err) {
            console.log("failed fetching activities...");
        },
    });
}
