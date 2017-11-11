import sys

sys.path.insert(0, "../lib")
import Leap
import select

from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

is_calibrated = False
corners = []
origin = None
dimension = None
is_hand_present = False



class SampleListener(Leap.Listener):
    def on_connect(self, controller):
        print "Connected"

    def on_frame(self, controller):
        global is_hand_present

        frame = controller.frame()
        fingers = frame.fingers
        index = None
        tip_pos = None

        if is_hand_present and fingers.is_empty:
            is_hand_present = False
            print "no hand"

        elif not is_hand_present and not fingers.is_empty:
            is_hand_present = True
            print "HAND DETECTED"


        if not fingers.is_empty:
            index = fingers.finger_type(Leap.Finger.TYPE_INDEX)
            index = Leap.Finger(index[0])
            tip_pos = index.tip_position
            if not is_calibrated:
                calibrate(tip_pos)
            else:
                pos = refresh(tip_pos)
                print pos


def calibrate(pos):
    if select.select([sys.stdin, ], [], [], 0.0)[0]:
        sys.stdin.readline()
        corners.append(pos)
        print "CALIBRATED CORNERS: %i" %len(corners)

    if len(corners) == 4:
        global is_calibrated
        is_calibrated = True

        global origin
        origin_x = corners[0][1]
        origin_y = -corners[0][2]
        origin = [origin_x, origin_y]
        print "ORIGIN X: %i, ORIGIN Y: %s" % (origin[0], origin_y)

        global dimension
        X = corners[2][1] - origin_x
        Y = -corners[2][2] - origin_y
        dimension = [X, Y]
        print "DIM X: %i, DIM Y: %s" % (X, Y)


def refresh(tip_pos):
    #print tip_pos

    x = tip_pos[1]
    y = -tip_pos[2]
    X = max(0,min((x - origin[0])/dimension[0],1))
    Y = max(0,min((y-origin[1])/dimension[1],1))
    return [round(X,2),round(Y,2)]




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
