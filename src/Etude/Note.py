from Instrument import Instrument
from  random import random

class Note(Instrument):
    def __init__(self,istart):
        super(Note,self).__init__()
        super.istart = istart
        self.iseed = random()
    def __str__():
        return "i 1 %f %f \n"