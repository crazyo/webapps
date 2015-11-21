function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function _isCsrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function _isSameOrigin(url) {
    var host = document.location.host;
    var protocol = document.location.protocol;
    var srorigin = '//' + host;
    var origin = protocol + srorigin;
    return (url ==   origin || url.slice(0,   origin.length + 1) ==   origin + '/') ||
           (url == srorigin || url.slice(0, srorigin.length + 1) == srorigin + '/') ||
           !(/^(\/\/|http:|https:).*/.test(url));
}

function setHeaderCsrf(xhr, settings) {
    if (!_isCsrfSafeMethod(settings.type) && _isSameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
}
