$('#signup').click(function() {
  $('.pinkbox').css('transform', 'translateX(80%)');
  $('.signin').addClass('hidden');
  $('.signup').removeClass('hidden');
});

$('#signin').click(function() {
  $('.pinkbox').css('transform', 'translateX(0%)');
  $('.signup').addClass('hidden');
  $('.signin').removeClass('hidden');
});