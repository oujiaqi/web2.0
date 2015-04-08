var work = false;
var times = 0;
window.onload = function() {
    document.getElementById("end").onmouseover = end;
    document.getElementById("start").onclick = again;
    document.getElementById("start").onmouseover = start;
    document.getElementById("maze").onmouseleave = outside;
    var h = document.getElementsByClassName("boundary");
    for (var i = 0; i < h.length; i++)
        h[i].onmouseover = youlose;
}

function youlose() {
    if (work) {
        times++;
        var divs = document.getElementsByClassName("boundary");
        for (var i = 0; i < divs.length; i++) {
            divs[i].style.backgroundColor = "#ff8888";
        }
        var text = document.getElementById("status");
        text.innerHTML = "You lose";
    }
}

function start() {
    work = true;
}


function again() {
    var h = document.getElementsByClassName("boundary");
    for (var i = 0; i < h.length; i++)
        h[i].style.backgroundColor = "#eeeeee";
    times = 0;
    var text = document.getElementById("status");
    text.innerHTML = "Move your mouse over the \"S \" to begin.";
    work = true;
}

function end() {
    if (work && times == 0) {
        var text = document.getElementById("status");
        text.innerHTML = "You win";
        work = false;
    }
}


function outside() {
    if (work) {
        youlose();
    }
}

