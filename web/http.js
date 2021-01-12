function httpRequest(url, method, cb) {
    var xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4) cb(this.status, this.responseText);
    };

    xmlhttp.open(method, url, true);
    xmlhttp.send();
}
function handleHttpNotSuccessResult(prefix, status, responseText, doalert = true) {
    var msgerror = `[${prefix}] Request failed. status=${status}, response=${responseText}`;
    console.error(msgerror);
    if (doalert)
        alert(msgerror);
}