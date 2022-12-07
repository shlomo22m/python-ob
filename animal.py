import abc
from abc import ABC , abstractmethod

class Animal(ABC):


    __name= ''

    def __init__(self):
        self.time=0

    def sleep(self,time=0):
        self.time = time
        print("sleep in hours:"+str(self.time))

    def makesound(self,soud):
        self.sound=soud
        print(self.sound)

    @abc.abstractmethod
    def move(self):
        pass