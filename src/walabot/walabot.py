#!/usr/bin/env python

from threading import Thread, Lock
import WalabotAPI as wala
import json

class Walabot(Thread, Serializer):

    def __init__(self):
        Thread.__init__(self)
        Serializer.__init__(self)

        self.debug = False
        self.targets_l = []
        self.numberOfTargets = 0
        self.wala = wala.Init()

    def getWalabot(self):
        return self.wala

    def getTargets(self):
        return self. targets

    def startWalabot(self):
        self.wala.Start()

    def run(self):
        while True:
            self.wala.Trigger()

            targets = self.wala.GetSensorTargets()
            if targets:
                appStatus, calibrationProcess = self.wala.GetStatus()

                if debug :print (appStatus)
                if debug :print (calibrationProcess)

                for i, target in enumerate(targets):
                    t = TargetPoint(i,target)
                    mutex.acquire(1)
                    self.targets_l.append(t)
                    mutex.release()
            else:
                print('No Target Detected')

            self.targets_l = []


    def stopWalabot(self):
        self.wala.Stop()
        self.wala.Disconnect()

    def isInitialized(self):
        return self.wala.IsInitialized()

    def connectWalabot(self):
        if not self.isInitialized():
            raise Exception('Wala not Initialized!')
'''
        wala.SetSettingsFolder()
'''
        try:
            self.wala.ConnectAny()
        except WalabotError as err:
            if err.message == self.wala.WALABOT_INSTRUMENT_NOT_FOUND:
                print('Please connect your Walabot')
            else:
                print(err.message)
        raise Exception(err.message);

'''
        wala.SetProfile(wala.PROF_SENSOR)
        wala.SetDynamicImageFilter(wala.FILTER_TYPE_MTI)
'''
    def toJson(self):
        if debug : Serializer.serialize(self)
        return Serializer.serialize(self)
