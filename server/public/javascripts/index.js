var canvas = document.getElementById('paint');
var ctx = canvas.getContext('2d');

var sketch = document.getElementById('sketch');
var sketch_style = getComputedStyle(sketch);
canvas.width = window.innerWidth - 90;
canvas.height = 4000;
ctx.lineWidth = 8;
drawPages();

var mouse = {x: 0, y: 0};

canvas.addEventListener('mousemove', function (e) {
    mouse.x = e.pageX - this.offsetLeft;
    mouse.y = e.pageY - this.offsetTop;
}, false);

/* Drawing on Paint App */
ctx.lineJoin = 'round';
ctx.lineCap = 'round';

ctx.strokeStyle = "black";

function drawPages() {
  ctx.strokeStyle = "#e6e6e6"
  ctx.lineWidth = 6;
  ctx.setLineDash([10, 5]);
  for (var i = 1; i <= 3; i++) {
    ctx.beginPath();
    ctx.moveTo(0,1000 * i);
    ctx.lineTo(window.innerWidth - 90,1000 * i);
    ctx.stroke();
  }
  ctx.lineWidth = 8;
  ctx.setLineDash([]);
}

function getColor(colour) {
    ctx.strokeStyle = colour;
}

function getSize(size) {
    ctx.lineWidth = size;
}

canvas.addEventListener('mousedown', function (e) {
    ctx.beginPath();
    ctx.moveTo(mouse.x, mouse.y);

    canvas.addEventListener('mousemove', onPaint, false);
}, false);

canvas.addEventListener('mouseup', function () {
    canvas.removeEventListener('mousemove', onPaint, false);
}, false);

var onPaint = function () {
    ctx.lineTo(mouse.x, mouse.y);
    ctx.stroke();
};
