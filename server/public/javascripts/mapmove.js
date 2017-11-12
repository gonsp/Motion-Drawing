var boxes = new Array(4);
var curActiveRow = 0;
var curActiveCol = 0;

for (var i = 0; i < boxes.length; i++) {
  boxes[i] = new Array(4);
}

elements = document.getElementsByClassName('box');

for (var i = 0; i < elements.length; i++) {
  boxes[Math.floor(i / 4)][i % 4] = elements[i];
}
