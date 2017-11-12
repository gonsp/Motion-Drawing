var canScroll = true;

$(function() {
  document.addEventListener('gest', function(gesture) {
    if (gesture.left && curActiveCol >= 3) {
      return;
    } else if (gesture.right && curActiveCol <= 0) {
      return;
    } else if (gesture.down && curActiveRow <= 0) {
      return;
    } else if (gesture.up && curActiveRow >= 3) {
      return;
    }

    $(boxes[curActiveRow][curActiveCol]).removeClass('a-box')
    if (canScroll && gesture.left) {
      $.fn.fullpage.moveSlideRight();
      curActiveCol++;
    } else if (canScroll &&  gesture.right) {
      $.fn.fullpage.moveSlideLeft();
      curActiveCol--;
    } else if (canScroll &&  gesture.up) {
      $.fn.fullpage.moveSectionDown();
      curActiveRow++;
    } else if (canScroll) {
      $.fn.fullpage.moveSectionUp();
      curActiveRow--;
    }
    $(boxes[curActiveRow][curActiveCol]).addClass('a-box')
  }, false);
  gest.start();
});
