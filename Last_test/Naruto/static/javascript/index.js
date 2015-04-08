window.onload = function() {
	var icon = document.getElementById("header-icon");
	icon.onmouseover = changeiconyellow;
	icon.onmouseout = changeiconorigin;
	var imlink = document.getElementById("imlink");
	imlink.onmouseover = rotate;
	imlink.onmouseout = rerotate;
	var pic1 = document.getElementById("fi");
	var pic2 = document.getElementById("se");
	var pic3 = document.getElementById("th");
	var pic4 = document.getElementById("fo");
	pic1.onmouseover = on;
	pic1.onmouseout = out;
	pic2.onmouseover = on;
	pic2.onmouseout = out;
	pic3.onmouseover = on;
	pic3.onmouseout = out;
	pic4.onmouseover = on;
	pic4.onmouseout = out;
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

function on() {
	var s = this.children;
	s[0].style.opacity = "1";
	s[0].style.width = "105%";
	s[0].style.height = "105%";
	s[1].style.bottom = "45px";
}

function out() {
	var s = this.children;
	s[0].style.opacity = "0.8";
	s[0].style.width = "100%";
	s[0].style.height = "100%";
	s[1].style.bottom = "0px";
}

//site search
function search() {
	var s = document.getElementById("searchkey").value;
	window.open("http://www.baidu.com/s?wd=" + s + " site:narutoblog.sinaapp.com", "_top")
}