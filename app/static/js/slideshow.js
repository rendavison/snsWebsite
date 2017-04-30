$(document).ready(function(){
  if($window).width() >= 800) {
    $('.slideshow').slick({
      infinite: true,
      autoplay: true,
      arrows: false,
      speed: 500,
      fade: true,
      cssEase: 'linear',
    });
  }
});
