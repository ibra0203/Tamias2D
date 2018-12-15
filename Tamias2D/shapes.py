import abc
import collision

from Tamias2D.vec2 import *
class Shape(object):
    __metaclass__ = abc.ABCMeta

    def set_angle(self, angle_):
        self.angle = angle_
        self.colShape.angle = angle_

    def set_pos(self, pos_):
        self.pos = pos_
        self.colShape.pos = collision.Vector(pos_.x, pos_.y)

    def get_center(self):
        return self.colShape.get_centroid()


class Polygon(Shape):

    def __init__(self, pos_, verts_, angle_=0):
        self.verts = verts_
        self.pos = pos_
        self.angle = angle_
        self.colShape = collision.Poly(pos_, verts_, angle_)

    def get_verts(self):
        return self.colShape.points

    def vertsAsList(self):
        _verts = []
        for v in self.get_verts():
            _v = [v.x, v.y]
            _verts.append(_v)
        return _verts

class Box(Polygon):
    def __init__(self, min_, max_, angle_=0):
        if isinstance(min_, Vec2) and isinstance(max_, Vec2) and isinstance(angle_, (int,float)):
            self.min = min_
            self.max = max_
            self.angle = angle_
            self.colShape = collision.Poly.from_box((min_+max_)/2 , max_.x - min_.x, max_.y - min_.y )
            self.colShape.angle = angle_


class Circle(Shape):
    def __init__(self, position, radius):
        self.colShape = collision.Circle(position, radius)
        self.pos = position
        self.radius = radius

    def get_center(self):
        return self.pos


