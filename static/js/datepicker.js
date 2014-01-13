$("#datepicker").datepicker({
   onSelect: function(dateText, inst) { 
      var dateAsString = dateText; //the first parameter of this function
      var dateAsObject = $(this).datepicker( 'getDate' ); //the getDate method
   }
});
$(function() {
$( "#datepicker" ).datepicker();
});
