from Range import Range
from Instrument import Instrument
class InstrumentFactory(object):
    def __init__(self):
        self.iattack = Range(0.001,0.05)
        self.idur = Range(0.1,1)
        self.ipan = Range(0,1,False)
        self.ifreq1 = Range(50,4000)
        self.ifreq2 = Range(50,4000)
        self.ihness = Range(0,1,False)
        self.idist  = Range(0.25,2)
    def makeInstrument(self):
        instr = Instrument()
        instr.idur =   self.idur()
        instr.iattack =   self.iattack()
        instr.ipan = self.ipan()
        instr.ifreq1 = self.ifreq1()
        instr.ifreq2 = self.ifreq2()
        instr.ihness = self.ihness()
        instr.idist  = self.idist()
        return instr
