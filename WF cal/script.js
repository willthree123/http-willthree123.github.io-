function myFunction() {

var g=+document.getElementById("weight").value;
var l=+document.getElementById("legth").value;
var h=+document.getElementById("hour").value;
var h=+document.getElementById("min").value;
t=h*60+m
document.getElementById("price").innerHTML = '$'+Math.round(5 +  (0.4*(g+l)) + (0.1*t));
}