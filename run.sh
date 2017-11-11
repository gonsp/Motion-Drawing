#!/bin/bash

# Leap motion service
python2 leap/src/main.py&

# Trackpad service
# Build
# cd touchpad/TouchpadDrawing &&  xcodebuild
# Execute
./touchpad/TouchpadDrawing/build/Release/TouchpadDrawing&


# Webserver with canvas