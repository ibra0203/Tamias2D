from physicsengine.body import *
from enum import Enum
import matplotlib.pyplot as plt
import numpy as np
class Options(Enum):
    POSITION = "position"
    ROTATION = "rotation"
    VELOCITY = "velocity"
    ANGVEL = "angularVel"
    FORCE = "force"
    TORQUE = "torque"
    ACCEL = "accel"
    ANGACCEL ="angAccel"

class OutputOptions:
    def __init__(self):
        self.options = {
            Options.POSITION: False,
            Options.ROTATION: False,
            Options.VELOCITY: False,
            Options.ANGVEL: False,
            Options.FORCE: False,
            Options.TORQUE: False,
            Options.ACCEL: False,
            Options.ANGACCEL: False
        }
    def __getitem__(self, index):
        return  self.options[index]
    def enable_option(self, key):
        if key in self.options:
            self.options[key] = True

    def disable_option(self, key):
        if key in self.options:
            self.options[key] = False

class PhysicsOutput:
    def __init__(self, frequency = 2000, options = OutputOptions()):
        self.deltaTime = frequency
        self.elapsedTime = 0
        self.frequency = frequency
        self.bodies = []
        self.options = options
        self.plotter = None
        self.n=0
    def add_body(self, body):
        if isinstance(body, Body):
            self.bodies.append(body)

    def update(self, deltaTime):
        self.deltaTime += deltaTime*1000
        self.elapsedTime +=deltaTime*1000
        if self.deltaTime > self.frequency:
            self.deltaTime = 0
            self._print_output()
            if self.plotter != None:
                if not self.plotter.done:
                    self._add_frame_info()
                    if self.elapsedTime > self.plotter.timeToPlot:
                        self.plotter.done = True
                        self.plotter.plot()

    def _add_frame_info(self):
        i = 0
        for b in self.bodies:
            bInfo = dict()
            if self.options[Options.POSITION]:
                bInfo[Options.POSITION] = b.position
            if self.options[Options.VELOCITY]:
                bInfo[Options.VELOCITY] = b.velocity
            if self.options[Options.ACCEL]:
                bInfo[Options.ACCEL] = b.accel
            if self.options[Options.ROTATION]:
                bInfo[Options.ROTATION] = b.angle
            if self.options[Options.ANGVEL]:
                bInfo[Options.ANGVEL] = b.angularVel
            if self.options[Options.ANGACCEL]:
                bInfo[Options.ANGACCEL] = b.angularAccel
            if self.options[Options.FORCE]:
                bInfo[Options.FORCE] = b.force
            if self.options[Options.TORQUE]:
                bInfo[Options.TORQUE] = b.torque
            bTimeInfo = []
            sI = str(i)
            if sI in self.plotter.bodiesInfo:
                bTimeInfo = self.plotter.bodiesInfo[sI]
            bTimeInfo.append(bInfo)
            self.plotter.bodiesInfo[sI] = bTimeInfo
            i+=1
    def _print_output(self):
        i=0
        print("---------At n = {}---------".format(self.n))
        for b in self.bodies:
            print("==Body"+str(i)+": ")
            if self.options[Options.POSITION]:
                print("Pos: "+str(b.position))
            if self.options[Options.VELOCITY]:
                print("Vel: "+str(b.velocity))
            if self.options[Options.ACCEL]:
                print("Accel: "+str(b.accel))
            if self.options[Options.ROTATION]:
                print("Angle: "+str(b.angle))
            if self.options[Options.ANGVEL]:
                print("Angular Vel: "+str(b.angularVel))
            if self.options[Options.ANGACCEL]:
                print("Angular Accel: "+str(b.angularAccel))
            if self.options[Options.FORCE]:
                print("Affecting Force: "+str(b.force))
            if self.options[Options.TORQUE]:
                print("Affecting Force: "+str(b.torque))
            print("=========")

            i+=1
        self.n+=1

