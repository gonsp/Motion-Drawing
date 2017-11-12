from socketIO_client import SocketIO, LoggingNamespace

with SocketIO('localhost', 3000, LoggingNamespace) as socketIO:
    #socketIO.emit('calibrate',{'reading_status':is_reading})
    #socketIO.emit('hand detection')
    socketIO.emit('leap-event', {'x': 12.34, 'y': 56.78})
    socketIO.wait(seconds=0.1)
