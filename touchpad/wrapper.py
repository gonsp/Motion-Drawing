#!/usr/bin/env python
import sys
import subprocess
# from socketIO_client import SocketIO, LoggingNamespace

# socket = SocketIO('localhost', 3000, LoggingNamespace)

def main():
    process = subprocess.Popen(["./build/Release/FingerMgmt.app/Contents/MacOS/FingerMgmt"], stdout=subprocess.PIPE)
    for line in iter(process.stdout.readline, ''):
        sys.stdout.write(line)
        print(line)

if __name__ == "__main__":
    main()
