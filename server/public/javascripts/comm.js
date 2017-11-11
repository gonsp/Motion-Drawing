var socket = io();

socket.on('leap-event', function (data) {
    console.log('leap event');
});