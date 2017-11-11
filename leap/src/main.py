import sys

sys.path.insert(0, "../lib")
import Leap

from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture


class SampleListener(Leap.Listener):
    def on_connect(self, controller):
        print "Connected"

    def on_frame(self, controller):
        frame = controller.frame()
        fingers = frame.fingers
        index = None
        if not fingers.is_empty:
            index = fingers.finger_type(Leap.Finger.TYPE_INDEX)
            index = index[0]
            

        if frame.id %30 == 0:
            print(index)


                #print(len(list(fingers)))
                #finger = list(fingers)[0]
                #print(finger)

"""
    def on_frame(self, controller):
        frame = controller.frame()
        fingers = frame.fingers
        front_finger = Leap.Finger(fingers.frontmost)
        foremost = front_finger.joint_position(3)
        index = fingers.finger_type(Leap.Finger.TYPE_INDEX)
        if len(index) > 0:
            index_finger = index[0]
            x_i = index_finger.x
            z_i = index_finger.z
        else:
            z_i = 0
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
            print "Number: %d, Index z: %d, Z: %d" %(len(fingers), z_i, z)
"""
def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()
    controller.set_policy(Leap.Controller.POLICY_OPTIMIZE_HMD)

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
