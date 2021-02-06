$(document).ready(function(){
  var touch = $('#resp-menu');
  var menu = $('.kesponsive-navigan');

  $(touch).on('click', function(e) {
  e.preventDefault();
  menu.slideToggle();
  });

  $(window).resize(function(){
  var w = $(window).width();
  if(w > 767 && menu.is(':hidden')) {
  menu.removeAttr('style');
  }
  });

});
