$(document).ready(function(){
	$("#about-btn").dblclick(function(event) {
		alert("Click the button using JQuery");
	})
	$("p").hover(function() {
		$("this").css('color', 'red');
	},
	function() {
		$("this").css('color', 'blue');
	})
});