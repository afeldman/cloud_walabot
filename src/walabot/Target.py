#!/usr/bin/env python


class TargetPoint(Serializer):
    def __init__(self, index, target):
        Serializer.__init__(self)

        self.index = index
        self.x = target.xPosCm
        self.y = target.yPosCm
        self.z = target.zPosCm

    def toString(self):
        return str('Target #{}x:{}y:{}z:{}').format(self.index + 1,
                self.x, self.y, self.z)

    def toJson(self):
        if debug : Serializer.serialize(self)
        return Serializer.serialize(self)
