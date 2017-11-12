var socket = io();

socket.on('leap-event-client', function (data) {
    console.log('leap event');
    //ctx.clearRect(0, 0, canvas.width, canvas.height);
    //ctx.fillRect(data.x, data.y, 1, 1);
});