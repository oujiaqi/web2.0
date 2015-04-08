window.onload = main;
var time = 200;
var t;
var STR;
var loop = 0;
function main() {
    document.getElementById("start").onclick = start;
    document.getElementById("stop").onclick = stop;
    document.getElementById("animation").onclick = stop;
    document.getElementById("s").onclick = changesize;
    document.getElementById("m").onclick = changesize;
    document.getElementById("l").onclick = changesize;
    document.getElementById("turbo").onclick = turbo;
}



function start() {
    var displayarea = document.getElementById("displayarea");
    var start = document.getElementById("start");
    var stop = document.getElementById("stop");
    var select = document.getElementById("animation");
    start.disabled = true;
    stop.disabled = false;
    select.disabled = true;
    animation();
    move();
}


function stop() {
    clearTimeout(t);
    var displayarea = document.getElementById("displayarea");
    var start = document.getElementById("start");
    var stop = document.getElementById("stop");
    var select = document.getElementById("animation");
    start.disabled = false;
    stop.disabled = true;
    select.disabled = false;
    animation();
    displayarea.value = STR;
}

function animation() {
    var select = document.getElementById("animation");
    if (select.value == "blank")
        STR = blank;
    else if (select.value == "exercise")
        STR = exercise;
    else if (select.value == "juggler")
        STR = juggler;
    else if (select.value == "bike")
        STR = bike;
    else if (select.value == "dive")
        STR = dive;
    else
        STR = custom;
}

size = {
    "small" : "7pt",
    "medium" : "12pt",
    "large" : "24pt"
}


//bi bao han shu
function changesize() {
    var va = this.value;
    var displayarea = document.getElementById("displayarea");
    displayarea.style.fontSize = size[va];
}


function move() {
    var temp = STR.split("=====\n");
    if (loop >= temp.length) {
        loop = 0;
    }
    else {
        document.getElementById("displayarea").value = temp[loop++];
    }
    t = setTimeout("move()", time);
}

function turbo() {
    if (document.getElementById("turbo").checked)
        time = 50;
    else
        time = 200;
}

custom =
"     _____\n" + 
"     _[_]_^\n" + 
"   <{T + T}>\n" + 
"     \\(^)/\n" + 
"   // [+] \\\\\n" + 
"  ||  [+]  ||\n" + 
"  @  //=\\\\  @\n" + 
"    ((   ))\n" + 
"     #   #\n" + 
"  ~-~-~-~-~-~-~-~-\n" + 
"=====\n" + 
"     _____\n" + 
"     _[_]_^ \n" + 
"   <{T + T}>\n" + 
"     \\(^)/\n" + 
"   // [+] \\\\ \n" + 
"  ||  [+]  \\\\\n" + 
"   @ //=\\\\  @\n" + 
"    ((   ))\n" + 
"     #   #\n" + 
"  -~-~-~-~-~-~-~-~\n" + 
"=====\n" + 
"     _____\n" + 
"     _[_]_^\n" + 
"   <{* + *}>\n" + 
"     \\(~)/\n" + 
"   // [+] \\\\\n" + 
"   || [+]  \\\\\n" + 
"    @//=\\\\   @\n" + 
"    [[   ))\n" + 
"     m   #\n" + 
"  ~-~-~-~-~-~-~-~-\n" + 
"=====\n" + 
"     _____\n" + 
"     _[_]_^       \n" + 
"   <{7 + 7}>\n" + 
"     \\(~)/ \n" + 
"   // [+] \\\\\n" + 
"   \\\\ [+]  \\\\\n" + 
"     @/=\\\\   @ \n" + 
"     [[  )) \n" + 
"     m   #\n" + 
"  -~-~-~-~-~-~-~-~\n" + 
"=====\n" + 
"     _____\n" + 
"     _[_]_^\n" + 
"   <{7 + 7}>\n" + 
"     \\(-)/ \n" + 
"   // [+] \\\\ \n" + 
"   || [+]  \\\\\n" + 
"    @//=\\\\  @ \n" + 
"    ((   )) \n" + 
"     #   #\n" + 
"  ~-~-~-~-~-~-~-~-\n" + 
"=====\n" + 
"     _____\n" + 
"     _[_]_^ \n" + 
"   <{- + -}>\n" + 
"     \\(-)/ \n" + 
"   // [+] \\\\ \n" + 
"  ||  [+]  ||\n" + 
"   @ //=\\\\ @ \n" + 
"    ((   )) \n" + 
"     #   #\n" + 
"  -~-~-~-~-~-~-~-~\n" + 
"=====\n" + 
"     _____\n" + 
"     _[_]_^ \n" + 
"   <{- + -}> \n" + 
"     \\(w)/ \n" + 
"   // [+] \\\\ \n" + 
"  ||  [+]  || \n" + 
"  @  //=\\\\ @ \n" + 
"    ((   )) \n" + 
"     #   #\n" + 
"  ~-~-~-~-~-~-~-~-\n" + 
"=====\n" + 
"     _____\n" + 
"     _[_]_^ \n" + 
"   <{0 + o}> \n" + 
"     \\(w)/  \n" + 
"   // [+] \\\\\n" + 
"  //  [+] || \n" + 
"  @  //=\\\\@\n" + 
"    ((  ]]\n" + 
"     #  m\n" + 
"  -~-~-~-~-~-~-~-~\n" + 
"=====\n" + 
"     _____\n" + 
"     _[_]_^ \n" + 
"   <{0 + 7}>\n" + 
"     \\(o)/ \n" + 
"   // [+] \\\\ \n" + 
"  //  [+] //\n" + 
" @   //=\\@ \n" + 
"    ((  ]]\n" + 
"     #  m\n" + 
"  ~-~-~-~-~-~-~-~-\n" + 
"=====\n" + 
"     _____\n" + 
"     _[_]_^ \n" + 
"   <{p + p}> \n" + 
"     \\(O)/  \n" + 
"   // [+] \\\\ \n" + 
"  //  [+] || \n" + 
"  @  //=\\ @  \n" + 
"    ((  )) \n" + 
"     #  m\n" + 
"  -~-~-~-~-~-~-~-~\n" + 
"=====\n" + 
"     _____\n" + 
"     _[_]_^      \n" + 
"   <{q + q}>    \n" + 
"     \\(0)/     \n" + 
"   // [+] \\\\  \n" + 
"  ||  [+]  || \n" + 
"   @ //=\\\\ @ \n" + 
"    ((  ))  \n" + 
"     #  #\n" + 
"  ~-~-~-~-~-~-~-~-\n" + 
"=====\n" + 
"     _____\n" + 
"     _[_]_^ \n" + 
"   <{\" + \"}> \n" + 
"     \\(0)/\n" + 
"   // [+] \\\\\n" + 
"   || [+] ||   \n" + 
"    @((=))@  \n" + 
"     [[ ]] \n" + 
"     m  m\n" + 
"  -~-~-~-~-~-~-~-~\n";