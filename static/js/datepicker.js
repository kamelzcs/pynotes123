$(function() {
$("#datepicker").datepicker({
   onSelect: function(dateText, inst) { 
      var dateAsString = dateText; //the first parameter of this function
      var dateAsObject = $(this).datepicker( 'getDate' ); //the getDate method
      $("#form input[name=year]").val(dateAsObject.getFullYear());
      $("#form input[name=month]").val(dateAsObject.getMonth()+1);
      $("#form input[name=day]").val(dateAsObject.getDate());
   }
});
});
