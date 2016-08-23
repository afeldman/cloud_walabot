#!/user/bin/python
import WalabotAPI as wala
import json

class Serializer(object):
    @staticmethod
    def encode_obj(obj):
        if type(obj).__name__ =='instance':
            return obj.__dict__

    @staticmethod
    def serialize(obj):
        return json.dumps(obj, default=Serializer.encode_obj)

class TargetPoint:
    def __init__(self, index, target):
        self.index = index
        self.x = target.xPosCm
        self.y = target.yPosCm
        self.z = target.zPosCm
    def toJson(self):
        return Serializer.serialize(self)
    def toString(self):
        return str('Target #{}x:{}y:{}z:{}').format(self.index + 1,
                self.x, self.y, self.z)

def TargetsToAzure(targets):
    for i, target in enumerate(targets):
       t = TargetPoint(i,target)
       print(t.toJson())

if __name__ == "__main__":

    debug = True

    walabot_hub = 'walabot'

#    key_name = 'RootManageSharedAccessKey' # SharedAccessKeyName from Azure portal
#    key_value = '' # SharedAccessKey from Azure portal
#    sbs = ServiceBusService(service_namespace,
                #            shared_access_key_name=key_name,
                 #           shared_access_key_value=key_value)

#    sbs.create_event_hub(walabot_hub)

    wala.Init()
    wala.SetSettingsFolder()

    try:
        wala.ConnectAny()
    except WalabotError as err:
        if err.message == wala.WALABOT_INSTRUMENT_NOT_FOUND:
            print('Please connect your Walabot')
        else:
            print(err.message)

    wala.SetProfile(wala.PROF_SENSOR)
    wala.SetDynamicImageFilter(wala.FILTER_TYPE_MTI)

    wala.Start()

    while True:
        wala.Trigger()

        targets = wala.GetSensorTargets()
        if targets:
            appStatus, calibrationProcess = wala.GetStatus()

            if debug :print (appStatus)
            if debug :print (calibrationProcess)

            TargetsToAzure(targets)
        else:
            print('No Target Detected')

    wala.Stop()
    wala.Disconnect()
