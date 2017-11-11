import sys

sys.path.insert(0, "../lib")
import Leap
import select

from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

is_calibrated = False
corners = []
origin = None
dimension = None


class SampleListener(Leap.Listener):
    def on_connect(self, controller):
        print "Connected"

    def on_frame(self, controller):
        frame = controller.frame()
        fingers = frame.fingers
        index = None
        pos = None
        if not fingers.is_empty:
            index = fingers.finger_type(Leap.Finger.TYPE_INDEX)
            index = Leap.Finger(index[0])
            pos = index.tip_position
            if not is_calibrated:
                calibrate(pos)
            else:
                refresh(pos)


def calibrate(pos):
    if select.select([sys.stdin, ], [], [], 0.0)[0]:
        sys.stdin.readline()
        corners.append(pos)

    if len(corners) == 4:
        global is_calibrated
        is_calibrated = True

        global origin
        origin_x = corners[0][1]
        origin_y = - corners[0][2]
        origin = [origin_x, origin_y]

        global dimension
        X = corners[2][1] - origin_x
        Y = -corners[2][2] - origin_y
        dimension = [X, Y]


def refresh(pos):
    x = pos[1]
    y = -pos[2]
    


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

    while True:
        pass


if __name__ == "__main__":
    main()
