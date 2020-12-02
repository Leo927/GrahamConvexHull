from vertex import Vertex
from enum import Enum

class Orientation:
    CCW = 1 #counter-clock wise
    CW = -1 #clock wise
    COLLINEAR = 0
    LEFT = 1 #turn left, has the same meaning and value as CCW
    RIGHT = -1 #turn right, has the same meaning and value as CW


class RadialComparator:
    def __init__(self, anchor: Vertex):
        self.anchor = anchor

    def comp(self, lhs, rhs):
        area = self.__signed_area(self.anchor, lhs, rhs) 
        if area > 0:
            return Orientation.CCW
        elif area < 0:
            return Orientation.CW
        else:
            return Orientation.COLLINEAR

    def __signed_area(self, p1: Vertex, p2: Vertex, p3: Vertex):
        return (p1.x * p2.y - p2.x*p1.y + p3.x*p1.y - p1.x*p3.y + p2.x*p3.y - p3.x*p2.y)

    def isLess(self, lhs, rhs):
        return self.comp(lhs,rhs) == Orientation.LEFT
