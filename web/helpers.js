function addZeroes(num) {
    // Cast as number
    var num = Number(num);
    // If not a number, return 0
    if (isNaN(num)) {
        return 0;
    }
    // If there is no decimal, or the decimal is less than 2 digits, toFixed
    if (String(num).split(".").length < 2 || String(num).split(".")[1].length <= 2) {
        num = num.toFixed(2);
    }
    // Return the number
    return num;
}

function elapsedTimeStrToMs(str) {
    const regex = new RegExp(/([0-9]*):([0-9]*):([0-9]*)/);
    const res = regex.exec(str);

    const hour = res[1] * 60 * 60 * 1000;
    const min = res[2] * 60 * 1000;
    const sec = res[3] * 1000;

    return hour + min + sec;
}

function elapsedTimeMsToFriendlyStr(elapsed) {

    var msPerMinute = 60 * 1000;
    var msPerHour = msPerMinute * 60;
    var msPerDay = msPerHour * 24;
    var msPerMonth = msPerDay * 30;
    var msPerYear = msPerDay * 365;

    if (elapsed < msPerMinute) {
        return Math.round(elapsed / 1000) + ' secs';
    }

    else if (elapsed < msPerHour) {
        return Math.round(elapsed / msPerMinute) + ' mins';
    }

    else if (elapsed < msPerDay) {
        return Math.round(elapsed / msPerHour) + ' hours';
    }

    else if (elapsed < msPerMonth) {
        return Math.round(elapsed / msPerDay) + ' days';
    }

    else if (elapsed < msPerYear) {
        return Math.round(elapsed / msPerMonth) + ' months';
    }

    else {
        return Math.round(elapsed / msPerYear) + ' years';
    }
}

function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}