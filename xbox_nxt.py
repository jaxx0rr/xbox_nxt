import nxt.locator
from nxt.sensor import *
from nxt.motor import *

from inputs import get_gamepad
import math
import threading

import os

class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    def __init__(self):

        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()


    def read(self): # return the buttons/triggers that you care about in this methode
        x = self.LeftJoystickX
        y = self.RightTrigger
        a = self.A
        b = self.X # b=1, x=2
        rb = self.RightBumper
        return [x, y, a, b, rb]

    def get_acc(self):
        return self.RightTrigger
        
    def get_rev(self):
        return self.LeftTrigger

    def get_dir(self):
        return self.LeftJoystickX

    def get_b(self):
        return self.B

    def _monitor_controller(self):
        while True:
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                elif event.code == 'BTN_TR':
                    self.RightBumper = event.state
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                elif event.code == 'BTN_NORTH':
                    self.X = event.state
                elif event.code == 'BTN_WEST':
                    self.Y = event.state
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                elif event.code == 'BTN_THUMBL':
                    self.LeftThumb = event.state
                elif event.code == 'BTN_THUMBR':
                    self.RightThumb = event.state
                elif event.code == 'BTN_SELECT':
                    self.Back = event.state
                elif event.code == 'BTN_START':
                    self.Start = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY1':
                    self.LeftDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY2':
                    self.RightDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY3':
                    self.UpDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY4':
                    self.DownDPad = event.state




if __name__ == '__main__':

    joy = XboxController()
    with nxt.locator.find(name="Bender") as b:
        print(b.get_device_info()[0:2])
        #print(b.get_battery_level())
        b.keep_alive()
        #b.play_tone_and_wait(400, 400)
        md = Motor(b, Port(0))
        ma = Motor(b, Port(1))
        #m.turn(50, 360)
        
         #non blocking
        #time.sleep(2) 
        #m.brake()
        while True:
            os.system("cls")
            acc = round(joy.get_acc()*100)
            rev = round(joy.get_rev()*100)
            dir = round(joy.get_dir()*100)
            print(str(acc)+" - "+str(rev)+" - "+str(dir))
            
            if (acc > 5):
                ma.run(-acc)
            elif (rev > 5):
                ma.run(rev)
            else:
                ma.idle()
                
            if (dir < -50):
                md.weak_turn(-75, 20)
                time.sleep(0.5)
                md.idle()
            elif (dir > 50):
                md.weak_turn(75, 20)
                time.sleep(0.5)
                md.idle()
            else:
                md.idle()
                
            if joy.get_b() == 1:
                quit()