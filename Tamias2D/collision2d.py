from collision import *
from Tamias2D.body import *
from Tamias2D.shapes import *
from Tamias2D.vec2 import *

class CollisionHandler:
    def __init__(self):
        return
    @classmethod
    def resolve_collision(self, a, b, resp):
        #relative velocity
        rv = b.velocity - a.velocity
        #relative velocity in terms of normal direciton
        normal = Vec2(resp.overlap_n.x, resp.overlap_n.y)

        velAlongNormal = Vec2.dot(rv, normal)
        # do not resolve if velocity is separating
        if (velAlongNormal > 0):
            return;

        # calculate restitution
        e = min(a.restitution, b.restitution)

        # impulse scalar
        j = -(1 + e) * velAlongNormal
        j /= (a.inv_mass +  b.inv_mass)
        # Apply impulse
        impulse = normal * j

        if resp.overlap_n.x == 0.0 and resp.overlap_n.y == 1.0:
            a.isBotCol = True
        if resp.overlap_n.x == 0.0 and resp.overlap_n.y == -1.0:
            b.isBotCol = True

        if a.bodyType == Body.DYNAMIC:
            a.velocity -= impulse * a.inv_mass

        if b.bodyType == Body.DYNAMIC:
            b.velocity += impulse * b.inv_mass


        self.pos_correction(a, b, resp)
        if a.bodyType != Body.STATIC and b.bodyType != Body.STATIC:
           self.rot_response(a, b, resp)

        if self._is_intersecting_with(a, b):
            return False
        else:
            return True

    @classmethod
    def rot_response(self, a, b, resp):
        Cp = a.shape.get_center()
        aCp = Vec2(Cp.x, Cp.y)
        bCp = b.shape.get_center()
        bCp = Vec2(bCp.x, bCp.y)

        n = self._get_col_point(a,b)
        aR = (aCp.x * (n.x) - aCp.y * (n.y)) / max(1, (aCp).mag())
        a.set_angular_accel(aR )

    @classmethod
    def _get_col_point(cls, a, b):
        colPoint = a.position
        if b.bodyType == Body.DYNAMIC:
            if isinstance(a.shape, Polygon) or isinstance(a.shape, Box):
                aPoints = a.shape.colShape.points
                for p in aPoints:
                    if isinstance(b.shape, Polygon) or isinstance(b.shape, Box):
                        if point_in_poly(p, b.shape.colShape):
                            colPoint = p
                    else:
                        if point_in_circle(p, b.shape.colShape):
                            colPoint = p
        return colPoint
    @classmethod
    def _is_intersecting_with(self, a, b):
        if isinstance(a.shape, Polygon) or isinstance(a.shape, Box):
            aPoints = a.shape.colShape.points
            for p in aPoints:
                if isinstance(b.shape, Polygon) or isinstance(b.shape, Box):
                    if point_in_poly(p, b.shape.colShape):
                        return True
                else:
                    if point_in_circle(p, b.shape.colShape):
                        return True
        return  False
    @classmethod
    def pos_correction(self, a, b, resp):
        percent = 0.8
        slop = 0.1
        if a.bodyType == Body.STATIC or b.bodyType == Body.STATIC:
            _st = a
            _dynamic = b

        penetration = Vec2(abs(resp.overlap_v.x), abs(resp.overlap_v.y)).mag() - slop
        if penetration < 0:
            penetration = 0
        correction = (penetration / (a.inv_mass + b.inv_mass)) * percent * (Vec2(resp.overlap_n.x, resp.overlap_n.y))
        if a.bodyType == Body.DYNAMIC:
            a.position -= correction * a.inv_mass
        if b.bodyType == Body.DYNAMIC:
            b.position += correction * b.inv_mass