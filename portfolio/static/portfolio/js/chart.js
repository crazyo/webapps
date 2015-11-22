function startListening() {

    $("path").click(function() {
        var elements = document.getElementsByTagName("g");
        for (var i = 0; i < elements.length; i++) {
            alert(elements[i]);
        }
    });
}
