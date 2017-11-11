import sys
sys.path.insert(0, "../lib")
import Leap

from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

def main():
    controller = Leap.Controller()

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()