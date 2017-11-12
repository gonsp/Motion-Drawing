import sys
from socketIO_client import SocketIO, LoggingNamespace

sys.path.insert(0, "../lib")
import Leap
import select

from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

is_calibrated = False
corners = []
origin = None
dimension = None
is_hand_present = False

socket = SocketIO('localhost', 3000, LoggingNamespace)


class SampleListener(Leap.Listener):
    def on_connect(self, controller):
        print "Connected"

    def on_frame(self, controller):
        global is_hand_present

        frame = controller.frame()
        fingers = frame.fingers

        if is_hand_present and fingers.is_empty:
            is_hand_present = False
            socket.emit('hand_detection', {'hand-detected': is_hand_present})
            print "no hand"

        elif not is_hand_present and not fingers.is_empty:
            is_hand_present = True
            socket.emit('hand_detection', {'hand-detected': is_hand_present})
            print "HAND DETECTED"

        if not fingers.is_empty:
            index = fingers.finger_type(Leap.Finger.TYPE_INDEX)
            index = Leap.Finger(index[0])
            tip_pos = index.stabilized_tip_position

            if not is_calibrated:
                calibrate(tip_pos)
            else:
                pos = refresh(tip_pos)
                print pos
                socket.emit('leap-event', {'x': pos[0], 'y': pos[1]})


def calibrate(pos):
    global corners

    if select.select([sys.stdin, ], [], [], 0.0)[0]:
        sys.stdin.readline()
        corners.append(pos)
        print "CALIBRATED CORNERS: %i, CORNER %i: X: %i Y: %i" % \
              (len(corners), len(corners), corners[-1][1], -corners[-1][2])
        socket.emit('calibrated-corners', {'num_corners': len(corners)})

    if len(corners) == 4:
        global is_calibrated
        is_calibrated = True

        global origin
        origin_x = corners[0][1]
        origin_y = -corners[0][2]
        origin = [origin_x, origin_y]
        print "ORIGIN X: %i, ORIGIN Y: %s" % (origin_x, origin_y)

        global dimension
        x_pos = corners[2][1] - origin_x
        #x1_pos = corners[1][1] - origin_x

        y_pos = -corners[2][2] - origin_y
        #y1_pos = -corners[3][2] - origin_y
        # if abs(x_pos - x1_pos) > 20 or abs(y_pos - y1_pos) > 20:
        #     corners = []
        #     is_calibrated = False
        #     print "RECALIBRATE"
        #     socket.emit('calibrated-corners', {'num_corners': len(corners)})


        dimension = [x_pos, y_pos]
        #else:
            #dimension = [(x_pos + x1_pos) / 2.0, (y_pos + y1_pos) / 2.0]

            #print "DIM X: %i, DIM Y: %s" % ((x_pos + x1_pos) / 2.0, (y_pos + y1_pos) / 2.0)


def refresh(tip_pos):
    # print tip_pos

    x = tip_pos[1]
    y = -tip_pos[2]
    x_pos = max(0, min((x - origin[0]) / dimension[0], 1))
    y_pos = max(0, min((y - origin[1]) / dimension[1], 1))
    return [round(x_pos, 2), round(y_pos, 2)]


def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()
    controller.set_policy(Leap.Controller.POLICY_OPTIMIZE_HMD)
    controller.set_policy(Leap.Controller.POLICY_BACKGROUND_FRAMES)

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    while True:
        pass


if __name__ == "__main__":
    main()
