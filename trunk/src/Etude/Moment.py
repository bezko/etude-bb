from MomentFactory import MomentFactory
from InstrumentFactory import InstrumentFactory
from Phrase import Phrase
from random import *
from Utils import exprandint
class Moment(MomentFactory):
    def __init__(self,start,duration):
        self.start=start
        self.duration =duration
        self.parts = exprandint(2,8)
        self.bars = exprandint(4,16)
        self.sco = ""
        f = InstrumentFactory()
        phrases = []
        for i in range(self.parts):
            p = Phrase(f,self.start,self.duration,self.bars)
            phrases.append(p)
            self.sco += p.sco



