var token = "0ecfcb9c5e3faf114107b70a9c9a3f85";
var x = 15;
var y = 15;
var listId = 4658;
var t = [0, 0, 0, 0, 2, 0];

function sendRequest(x, y, listId, troops) {
    fetch("https://ts15.hispano.travian.com/ajax.php?cmd=raidList", {
        "credentials": "include",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Request": "JSON",
            "X-Requested-With": "XMLHttpRequest"
        },
        "referrer": "https://ts15.hispano.travian.com/build.php?tt=99&id=39",
        "method": "POST",
        "mode": "cors",
        "body": "cmd=raidList&method=ActionAddSlot&listId=" + listId + "&slotId=&x=" + x + "&y=" + y
            + "&t1=" + troops[0] + "&t2=" + troops[1] + "&t3=" + troops[2] + "&t4=" + troops[3] + "&t5=" +
            troops[4] + "&t6=" + troops[5] + "&t7=0&t8=0&t9=0&t10=0&ajaxToken=" + token
    });
}


function run(a, listId, troops) {
    for (var i = 0; i < a.length; i++) {
        console.log(sendRequest(a[i][0], a[i][1]), listId, troops);
    }
}


//get lists
function printRaidLists() {
    var listIds = document.getElementsByName("lid");
    var str = "[";
    for (var i = 0; i < listIds.length; i++) {
        str += "[" + listIds[i].defaultValue + "],"
    }
    str = str.substr(0, str.length - 1);
    str += "]";
    console.log(str);
}

printRaidLists();

