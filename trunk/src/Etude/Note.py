import Instrument
from  random import random

class Note(Instrument.Instrument):
    def __init__(self,istart):
        super(Note,self).__init__()
        self.istart = istart
        self.iseed = random()
    def __str__(self):
        return "i 1 %f %f %f %f %f %f %f %f %f\n" % (self.istart,self.idur,self.ipan,self.iattack,self.ifreq1,self.ifreq2,self.ihness,self.idist,self.iseed)