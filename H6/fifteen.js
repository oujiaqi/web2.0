window.onload = function() {
    var puzzlearea = document.getElementById("puzzlearea");
    var Shuffle = document.getElementById("shufflebutton");
    //counter of steps
    var usedsteps = 0;
    //time of use
    var usedtime = 0;
    //a judge for no cheating
    var reset = false;
    //time T
    var T;
    //display pic area
    var picdisplay = document.createElement("div");
    document.getElementById("overall").appendChild(picdisplay);
    picdisplay.style.position = "absolute";
    picdisplay.style.top = "250px";
    picdisplay.style.left = "50px";
    picdisplay.style.width = "150px";
    picdisplay.style.height = "150px";
    picdisplay.style.backgroundSize = "100% 100%";
    picdisplay.style.backgroundImage = "url('picture1.jpg')";



    var controls = document.getElementById("controls");

    //create blank
    var blank = document.createElement("div");
    puzzlearea.appendChild(blank);
    var pieces = puzzlearea.children;
    setposition(pieces);

    //create select_button
    var select_button = document.createElement("select");
    for (var i = 1; i <= 7; i++) {
        var options = document.createElement("option");
        options.value = "picture" + i + ".jpg";
        options.text = "picture" + i;
        select_button.appendChild(options);
    };
    controls.appendChild(select_button);

    //creat show time area & steps counter area
    var timearea = document.createElement("button");
    var stepsarea = document.createElement("button");
    timearea.innerHTML = "Time: 0s";
    stepsarea.innerHTML = "Steps: 0";
    controls.appendChild(timearea);
    controls.appendChild(stepsarea);

    //select a picture
    function selectpic() {
        for (var i = 0; i < pieces.length; i++) {
            pieces[i].style.backgroundImage = "url(" + select_button.value + ")";
        }
        clearTimeout(T);
        usedsteps = 0;
        usedtime = 0;
        timearea.innerHTML = "Time: 0s";
        stepsarea.innerHTML = "Steps: 0";
        picdisplay.style.backgroundImage = "url(" + select_button.value + ")";
    };

    //set pieces position. also set the blank
    function setposition() {
        for (var i = 0; i < pieces.length; i++) {
            pieces[i].classList.add("puzzlepiece");
            var x = Math.floor(i/4)*100;
            var y = Math.floor(i%4)*100;
            pieces[i].style.top = x + "px";
            pieces[i].style.left = y + "px";
            pieces[i].style.backgroundPosition = "-" + y + "px -" + x + "px";
        }
        pieces[pieces.length-1].style.visibility = "hidden";
    };

    // piece is valid to move
    function isvalid(test) {
        if (test.style.top == blank.style.top &&
            Math.abs(parseInt(test.style.left)-parseInt(blank.style.left)) == 100 ||
            test.style.left == blank.style.left &&
            Math.abs(parseInt(test.style.top)-parseInt(blank.style.top)) == 100)
            return true;
        return false;
    };

    //light up valid piece
    function lightup() {
        if (isvalid(this))
            this.classList.add("movablepiece");
    };

    //remove the added class
    function lightoff() {
        this.classList.remove("movablepiece");
    };

    //exchange two div
    function exchange(div1, div2) {
        var top = div1.style.top;
        var left = div1.style.left;
        div1.style.top = div2.style.top;
        div1.style.left = div2.style.left;
        div2.style.top = top;
        div2.style.left = left;
    };

    //change the piece when click
    function clickmove() {
        if (isvalid(this)) {
            if (usedsteps == 0) {
                timer();
            }
            exchange(this, blank);
            usedsteps++;
            stepsarea.innerHTML = "Steps: " + usedsteps;
            succeed();
        }
    };

    //reset pieces
    function shuffle() {
        for (var i = 0; i < 500; i++) {
            var test = Math.floor(Math.random() * 16);
            if (isvalid(pieces[test])) {
                exchange(pieces[test], blank);
            }
        }
        clearTimeout(T);
        usedsteps = 0;
        usedtime = 0;
        timearea.innerHTML = "Time: 0s";
        stepsarea.innerHTML = "Steps: 0";
        reset = true;
    };

    //judge is finish or not
    function isfinished() {
        for (var i = 0; i < pieces.length; i++) {
            if (pieces[i].style.top != Math.floor(i/4)*100 + "px" ||
                pieces[i].style.left != Math.floor(i%4)*100 + "px")
                return false;
        }
        return true;
    };

    //timer
    function timer() {
        timearea.innerHTML = "Time: " + usedtime + "s";
        usedtime++;
        T = setTimeout(timer, 1000);
    };

    //succeed
    function succeed() {
        if (isfinished() && reset) {
            clearTimeout(T);
            alert("Congratulation! You finish in " + (usedtime - 1) +"s in " + usedsteps + " steps");
            reset = false;
        }
    };

     //when work
    for (var i = 0; i < pieces.length; i++) {
        pieces[i].onmouseover = lightup;
        pieces[i].onmouseout = lightoff;
        pieces[i].onclick = clickmove;
        pieces[i].style.transition = "all 0.4s";
    };
    Shuffle.onclick = shuffle;
    select_button.onchange = selectpic;
}









