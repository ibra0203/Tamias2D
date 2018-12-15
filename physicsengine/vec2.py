import math
class Vec2:
    PI = 3.14159265358979323846
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        types = (int, float)
        if isinstance(other, types):
            x = self.x + other
            y = self.y + other
        else:
            x = self.x + other.x
            y = self.y + other.y
        return Vec2(x,y)
    def __sub__(self, other):
        types = (int, float)
        if isinstance(other, types):
            x = self.x - other
            y = self.y - other
        else:
            x = self.x - other.x
            y = self.y - other.y
        return Vec2(x, y)
    def __mul__(self, other):
        types = (int, float)
        if isinstance(other, types):
            x = self.x * other
            y = self.y * other
        else:
            x = self.x * other.x
            y = self.y * other.y
        return Vec2(x, y)
    def __rmul__(self, other):
        types = (int, float)
        if isinstance(other, types):
            x = self.x * other
            y = self.y * other
        else:
            x = self.x * other.x
            y = self.y * other.y
        return Vec2(x, y)
    def __truediv__(self, other):
        types = (int, float)
        if isinstance(other, types):
            if other ==0:
                other=1
            x = self.x / other
            y = self.y / other
        else:
            x = self.x / other.x
            y = self.y / other.y
        return Vec2(x, y)
    def __str__(self):
        s = "({}, {})".format(round(self.x, 2), round(self.y, 2))
        return s
    def __eq__(self, other):
        if isinstance(other, Vec2):
            if self.x == other.x and self.y == other.y:
                return True
        return False
    def getX(self):
        return round(self.x, 2)
    def getY(self):
        return round(self.y, 2)
    def mag(self):
       return math.sqrt(self.x * self.x + self.y * self.y)
    @classmethod
    def cross(cls, a, b):
        z = (a.x * b.y) - (a.y * b.x)
        return Vec2(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x)
    @classmethod
    def dot(self, a, b):
        return (a.x * b.x) + (a.y * b.y)

    @classmethod
    def rotate(self, theta, v):
        n = Vec2(0,0,1)
        theta = theta * 180 / Vec2.PI
        return v * math.cos(theta) + n * Vec2.dot(v,n) * (1.0 - math.cos(theta)) + Vec2.cross(n,v) * math.sin(theta)

Vec2.DOWN = Vec2(0,1)
Vec2.UP = Vec2(0,-1)
Vec2.LEFT = Vec2(-1,0)
Vec2.RIGHT = Vec2(1,0)