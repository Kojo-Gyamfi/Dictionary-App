window.onload = function () {
  $('.sidenav a').click(function () {
    $('.sidenav a').removeClass('side-active');
      $(this).addClass('side-active');
  })
};
