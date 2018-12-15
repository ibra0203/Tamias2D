from Tamias2D.vec2 import *

class Body:
    STATIC = 0
    DYNAMIC = 1
    def __init__(self, position_, mass_, inertia_, shape_, angle=0, bodyType_= DYNAMIC, restitution_ = 0):
        self.position = position_
        self.mass = mass_
        self.inv_mass = 1/max(mass_, 0.1)
        self.force = Vec2(0,0)
        self.velocity = Vec2(0,0)
        self.lastVel = Vec2(0, 0)
        self.accel = Vec2(0,0)
        self.inertia = inertia_
        self.torque = 0
        self.lastTorque = 0
        self.angle = angle
        self.lastAngle = angle
        self.angularVel = 0
        self.angularAccel=0
        self.bodyType = bodyType_
        self.shape = shape_
        self.shape.set_pos(position_)
        self.shape.set_angle(angle)
        self.gravity = Vec2(0,0)
        self.restitution = restitution_
        self.isBotCol = False

    #in: deltaTime(float)
    #out: void
    def update(self, deltaTime):
        if self.bodyType == Body.DYNAMIC:
            self.angleAccelNorm =  0.3 * deltaTime
            angleAccelNorm = self.angleAccelNorm
            if self.angle > 0:
                angleAccelNorm = abs(angleAccelNorm) * -1
            if self.angle > -.009 and self.angle < .009:
                angleAccelNorm = 0

            self.angularAccel = (self.torque/self.inertia)
            self.angularVel += self.angularAccel * deltaTime
            self.angle += self.angularVel * deltaTime


            gravity = self.gravity
            if self.isBotCol:
                gravity=Vec2(0,0)
            self.thrust = self.force
            self.accel = (self.thrust / self.mass) + gravity*deltaTime

            self.lastVel = self.velocity
            self.velocity += self.accel * deltaTime
            self.position += ((self.velocity + self.lastVel) * 0.5) * deltaTime

            self.shape.set_pos(self.position)
            self.shape.set_angle(self.angle)

            if self.force.mag() < 0.000000005:
                self.force = Vec2(0,0)
            if self.torque < 0.000000005:
                self.torque = 0
                self.angularVel =0
            if self.accel.mag() < 0.000000005:
                self.accel = Vec2(0,0)
            if self.velocity.mag() < 0.000000005:
                self.velocity = Vec2(0,0)

                self.lastTorque = self.torque

        else:
            self.velocity=Vec2(0,0)
            self.accel =Vec2(0,0)
            self.torque = 0
        self.lastDeltaTime = deltaTime

    #input: force_ (Vec2)
    def apply_force(self, force_):
        force_ = force_
        self.force += force_

    #input: torque_ (float)
    def apply_torque(self, torque_):
        self.torque += torque_

    # input: torque_ (float)
    def set_torque(self, torque_):
        self.torque = torque_

    #input: space_ (Space)
    def set_space(self, space_):
        self.space = space_
        self.gravity = space_.gravity

    #input: aV_(float)
    def set_angular_accel(self, aV_):
        aAc = aV_/self.lastDeltaTime
        torque_ = self.inertia * aAc *0.01
       # if(abs(self.torque - torque_) <100):
        if self.lastTorque == 0:
            self.lastTorque = torque_
            self.set_torque(torque_)
        else:
            if abs(torque_  - self.lastTorque) > 100:
                self.lastTorque = torque_
                self.set_torque(torque_)










