var socket = io();

socket.on('leap-event-client', function (data) {
    var screenY = data.y * window.innerHeight;
    var screenX = data.x * window.innerWidth;
    console.log(screenX);
    console.log(screenY);
    $("#pointerImg").css({'top' : screenY + 'px', 'left' : screenX + 'px' });
});