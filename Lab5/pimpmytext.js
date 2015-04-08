var size = 12;

window.onload = main;

function $(id) {
    return document.getElementById(id);
}


function main() {
    $("bigger").onclick=bigger;
    $("bling").onclick=bling;
    $("snoopify").onclick=snoopify;
    $("malkovitch").onclick=malkovitch;
    $("igpay atinlay").onclick=IgpayAtinlay;
    $("empty").onclick=empty;
}


function bigger() {
    var text = $("text");
    size += 1;
    text.style.fontSize = size + "pt";
    if (size < 24)
        setTimeout("bigger()", 500);
};


function bling() {
    var text = $("text");
    var bling = $("bling");
    if (bling.checked) {
        text.className = "blingChange";
        $("body").style.backgroundImage = "url(hundred-dollar-bill.jpg)";
    }
    else {
        text.className = "";
        $("body").style.backgroundImage = "none";
    }
}


function snoopify() {
    var text = $("text");
    var str = text.value.toUpperCase().replace(".", "-izzle.");
    text.value = str;
}


function malkovitch() {
    var text = $("text");
    var str = text.value.replace(/\w{5,}/g,"Malkovitch");
    text.value = str;
}


function IgpayAtinlay() {
    var text = $("text");
    var te = text.value;
    var str = te.match(/\w+/g);
    te = te.replace(/\w+/g, "*");
    for (var i = 0; i < str.length; i++) {
        if (str[i].match(/\b[a|e|i|o|u]+/i)) {
            te = te.replace("*",str[i]+"-ay");
        }
        else {
            te = te.replace("*",str[i].slice(1)+str[i].charAt(0)+"-ay");
        }
    }
    text.value = te;
}


function empty() {
    var text = $("text");
    text.value = "";
}

