$('#sign_up').click(function() {
  $('.login-move_box').css('transform', 'translateX(80%)');
  $('.sign_in').addClass('login-hidden');
  $('.sign_up').removeClass('login-hidden');
});

$('#sign_in').click(function() {
  $('.login-move_box').css('transform', 'translateX(0%)');
  $('.sign_up').addClass('login-hidden');
  $('.sign_in').removeClass('login-hidden');
});