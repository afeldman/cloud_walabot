#!/usr/bin/env python

from threading import Thread, Lock
import WalabotAPI as walabot
import json
import posix_ipc as ipc

class Walabot(Thread, Serializer):

    def __init__(self,memory_name="/walabot_ipc", psize = ipc.PAGE_SIZE):
        Thread.__init__(self)
        Serializer.__init__(self)

        self.debug = False
        self.targets_l = []
        self.numberOfTargets = 0

        self.wala = walabot.Init()

        self.shm = Shm(memory_name,psize)

    def getWalabot(self):
        return self.wala

    def getTargets(self):
        return self.targets_l

    def startWalabot(self):
        self.wala.Start()

    def run(self):
        while True:
            self.wala.Trigger()

            targets = walabot.GetSensorTargets()
            if targets:
                appStatus, calibrationProcess = walabot.GetStatus()

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
        try:
            self.wala.ConnectAny()
        except WalabotError as err:
            if err.message == walabot.WALABOT_INSTRUMENT_NOT_FOUND:
                print('Please connect your Walabot')
            else:
                print(err.message)
        raise Exception(err.message);

    def toJson(self):
        if debug : Serializer.serialize(self)
        return Serializer.serialize(self)

    def Targets2Json(self):
        if debug : Serializer.serialize(self.targets_l)
        return Serializer.serialize(self.targets_l)

    def Targets2Shm(self,
                    memory_name,
                    sleeptimer= 0.05,
                    psize = ipc.PAGE_SIZE):

        self.shm.wait4receiver()
        self.shm.send(self.Targetst2Json(), sleeptime)
