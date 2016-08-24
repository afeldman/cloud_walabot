#!/usr/bin/env python

from time import sleep
import mmap
import posix_ipc as ipc

class Shm:
    def __init__(self, memory_name, psize):
        self.mn = memory_name
        self.shm = ipc.SharedMemory(self.mn,
                               ipc.O_CREX,
                               size=psize)

        self.memory = mmap.mmap(shm.fd, shm.size)

        self.shm.close_fd()
        self.sem = None

        self.isReceiverConnected = False
        self.debug = False

    def wait4receiver(self):
        while(True):
            try:
                sleep(1)
                self.sem = ipc.Semaphore(self.mn, flags = 0)
                # receiver is on hold. get the semaphore
                self.sem.acquire()
                self.isReceiverConnected = True
                break
            except Exception as err:
                self.isReceiverConnected = False
                print (err.message)

    def getShm(self):
        return self.shm

    def getMemory(self):
        return self.memory;

#Targets is a json string of the Targets form the walabot
    def send(self, targets):

        if not self.isReceiverConnected:
            raise Exception("No Receiver Connected")

        self.memory.seek(0)
        self.memory.write(targets)

        if self.debug : print("Sending Message: "+ targets)

        self.sem.release() # release lock
        sleep(sleeptimer)# ... and sleep to give chance for receiver to get the lock
        self.acquire()# wait for receiver to process the previous message and release the lock

    def close(self):
        try:
            self.memory.close()
        except:
            print "failed to close mmap"
        try:
            self.shm.unlink()
        except:
            print "failed to clean up shared memory"
        try:
            self.sem.close()
        except:
            print "failed to clean up semaphore"
