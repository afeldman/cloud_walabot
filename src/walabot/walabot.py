#!/usr/bin/env python

import WalabotAPI as wala
import json

debug = False

class Walabot(Object):

    def __init__(self):
        pass

    def toJson(self):
        return self.serialize(self)

    def encode_walabot(obj):
        if type(obj).__name__ =='instance':
            return obj.__dict__

    def serialize(obj):
        return json.dumps(obj, default=Serializer.encode_obj)
