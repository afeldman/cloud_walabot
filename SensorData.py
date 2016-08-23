#!/user/bin/python

import WalabotAPI as wala
from __future__ import print_function
from sys import platform
from os import system

import json

class Serializer(object):
    @staticmethod
    def encode_obj(obj):
        if type(obj).__name__ =='instance':
            return obj.__dict__

    @staticmethod
    def serialize(obj):
        return json.dumps(obj, default=Serializer.encode_obj)

class JTarget(object):
    def __init__(self, target):
        self.x = target.xPosCm
        self.y = target.yPosCm
        self.z = target.zPosCm

    def toJson(self):
        return Serializer.serialize(self)

if __name__ == "__main__":

    walabot_hub = 'walabot'

    key_name = 'RootManageSharedAccessKey' # SharedAccessKeyName from Azure portal
    key_value = '' # SharedAccessKey from Azure portal
    sbs = ServiceBusService(service_namespace,
                            shared_access_key_name=key_name,
                            shared_access_key_value=key_value)

    sbs.create_event_hub(walabot_hub)

    wala.Init()
    wala.SetSettingsFolder()
    wala.ConnectAny()

    wala.SetProfile(wala.PROF_SENSOR)
    wala.SetDynamicImageFilter(wala.FILTER_TYPE_MTI)

    wala.Start()

    while True:
        wala.Trigger()
        targets = wala.GetSensorTargets()

        for i, t in enumerate(targets):
            jtarget = JTarget(t)
            if debug: print (jtarget.toJson())
            sbs.send_event(walabot_hub, jtarget.toJson())

    wlbt.Stop()
    wlbt.Disconnect()
