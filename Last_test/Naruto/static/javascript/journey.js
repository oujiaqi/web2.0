window.onload = function() {
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

//add a post method
function postwith(to, p) {
	var myForm = document.createElement("form");
	myForm.method = "post";
	myForm.action = to;
	for ( var k in p) {
		var myInput = document.createElement("input");
		myInput.setAttribute("name", k);
		myInput.setAttribute("value", p[k]);
		myForm.appendChild(myInput);
	}
	document.body.appendChild(myForm);
	myForm.submit();
	document.body.removeChild(myForm);
}

function bigger() {
	var b = document.getElementById("LOVE");
	b.style.fontSize = "115%";
}

//site search
function search() {
	var s = document.getElementById("searchkey").value;
	window.open("http://www.baidu.com/s?wd=" + s + " site:narutoblog.sinaapp.com", "_top")
}