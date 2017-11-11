var canScroll = true;

$(function() {
  document.addEventListener('gest', function(gesture) {
    if (canScroll && gesture.left) {
      $.fn.fullpage.moveSlideRight();
    } else if (canScroll &&  gesture.right) {
      $.fn.fullpage.moveSlideLeft();
    } else if (canScroll &&  gesture.up) {
      $.fn.fullpage.moveSectionDown();
    } else if (canScroll) {
      $.fn.fullpage.moveSectionUp();
    }
  }, false);
  gest.start();
});
