import sys

sys.path.insert(0, "../lib")
import Leap

from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture


class SampleListener(Leap.Listener):
    def on_connect(self, controller):
        print "Connected"

    def on_frame(self, controller):
        frame = controller.frame()
        pointables = frame.pointables
        front_finger = Leap.Finger(pointables.frontmost)
        foremost = front_finger.joint_position(3)
        x = foremost.x
        y = foremost.y
        z = foremost.z
        if front_finger.type == 0:
            type = "thumb"
        elif front_finger.type == 1:
            type = "index"
        elif front_finger.type == 2:
            type = "middle"
        elif front_finger.type == 3:
            type = "ring"
        elif front_finger.type == 4:
            type = "pinky"
        else:
            type = "no finger"


        if frame.id %30 == 0:
            print "Frame id: %d, type: %s, hands: %d, X: %d, Y: %d, Z: %d" % (frame.id, type, len(frame.hands), x, y, z)


def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
