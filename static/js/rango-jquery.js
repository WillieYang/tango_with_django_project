$(document).ready(function(){
	$("#about-btn").dblclick(function(event) {
		alert("Click the button using JQuery");
		msgstr = $("#msg").html()
		msgstr = msgstr + "ooo"
		$("#msg").html(msgstr)
	});
	$("#about-btn").addClass('btn btn-primary')
	$("p").hover(function(event) {
		$(this).css('color', 'red');
	},
	function(event) { 
		// event seems can be commented...
		$(this).css('color', 'blue');
	});
});