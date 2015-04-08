window.onload = function() {
	changing();
	var icon = document.getElementById("header-icon");
	icon.onmouseover = changeiconyellow;
	icon.onmouseout = changeiconorigin;
	var imlink = document.getElementById("imlink");
	imlink.onmouseover = rotate;
	imlink.onmouseout = rerotate;
}

//change header icon pic to yellow
function changeiconyellow() {
	var icon = document.getElementById("header-icon");
	icon.src = "static/images/header-icon1.png";
	icon.style.transform = "rotate(360deg)"
}

//change header icon pic to origin

function changeiconorigin() {
	var icon = document.getElementById("header-icon");
	icon.src = "static/images/header-icon3.png";
	icon.style.transform = "none";
}

function rotate() {
	var ro = document.getElementById("headportrait");
	ro.style.transform = "rotate(360deg)";
}

function rerotate() {
	var ro = document.getElementById("headportrait");
	ro.style.transform = "none";
}

//site search
function search() {
	var s = document.getElementById("searchkey").value;
	window.open("http://www.baidu.com/s?wd=" + s + " site:narutoblog.sinaapp.com", "_top")
}


//antistops change
var T;
var COLOR = ["red", "yellow", "green", "blue", "brown", "chocolate", "orange", "darkred", "deeppink", "pink", "gold", "purple", "tomato"]
function changing() {
	var antistops = document.getElementById("antistops");
	items = antistops.children;
	for (var i = 0; i < items.length; i++) {
		var Rcolor = Math.floor(Math.random()*13);
		var Rsize = Math.floor(Math.random()*30) + 5;
		var Rleft = Math.floor(Math.random()*150)-70;
		var Rtop = Math.floor(Math.random()*450)-100;
		var Rotation = Math.floor(Math.random()*1500)-750;
		items[i].style.color = COLOR[Rcolor];
		items[i].style.top = Rtop + "px";
		items[i].style.left = Rleft + "%";
		items[i].style.fontSize = Rsize + "px";
		
	}
	T = setTimeout(changing, 1500);
}