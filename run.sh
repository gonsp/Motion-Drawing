#!/bin/bash

# Leap motion service
cd leap/src && python2 main.py&

# Trackpad service
# Build
# cd touchpad &&  xcodebuild
# Execute
./touchpad/build/Release/TouchpadDrawing&


# Webserver with canvas