#!/usr/bin/env python

import json

class Serializer(Object):
    def __init__(self):
        pass

    def encode_walabot(self,obj):
        if type(obj).__name__ =='instance':
            return obj.__dict__

    def serialize(self,obj):
        return json.dumps(obj, default=Serializer.encode_obj)

    def toJson(self):
        pass

    def toString(self):
        pass
