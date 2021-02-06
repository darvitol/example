var i = 2;
var pic = '';
var sum = 0;

let order = [];

// Обработчик чек-боксов
$('input:checkbox').click(function(){
	if ($(this).is(':checked')) {
		var name = ($(this).attr('name'));
    if (name == 'foundation') {
      var src = "<img id='"+ name +"-pic' src='img/toppings/"+name+".png' style='z-index:1; position:absolute;'>";
      sum = sum + parseInt($(this).val());
      $('#sum').html(sum);
      order.push($(this).next('label').text());
    } else {
      var src = "<img id='"+ name +"-pic' src='img/toppings/"+name+".png' style='z-index:"+i+"; position:absolute;'>";
      sum = sum + parseInt($(this).val());
      $('#sum').html(sum);
      order.push($(this).next('label').text());
    }
    $("#pizza-box").append(src);
	} else {
    var name = ($(this).attr('name'));
    $("#"+name+"-pic").remove();
    sum = sum - $(this).val();
    $('#sum').html(sum);
    order.slice($(this).next('label').text());
	}
  pic = "#"+name+"-pic";
});

// Очитстить всё
$("#clear").click(function(){
  $('body input:checkbox').prop('checked', false);
  $("#pizza-box").children().remove();
  sum = 0;
  $('#sum').html(sum);
  order = [];
})

$("#show-order").click(function(){
  for (pos=0; pos<order.length; pos++){
    $("#order").append("<ul><li class='order-list'>"+order[pos]+"</li></ul>");
  }
    $("#modal-summa").html(sum);
});
