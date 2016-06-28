$(document).ready(function(){
  $(".topbar a").each(function(){
    if($(this).prop('href') == window.location.href){
      $(this).addClass('current');
    }
  });
});
