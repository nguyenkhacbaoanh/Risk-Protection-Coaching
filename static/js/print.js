$( document ).ready(function() {
	setTimeout(function(){
		$( "#button-print" ).click(function() {
  			window.print();
		});
	}, 4000);
});