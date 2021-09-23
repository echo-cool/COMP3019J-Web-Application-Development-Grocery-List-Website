$('#sign_up').click(function() {
  $('.move_box').css('transform', 'translateX(80%)');
  $('.sign_in').addClass('hidden');
  $('.sign_up').removeClass('hidden');
});

$('#sign_in').click(function() {
  $('.move_box').css('transform', 'translateX(0%)');
  $('.sign_up').addClass('hidden');
  $('.sign_in').removeClass('hidden');
});