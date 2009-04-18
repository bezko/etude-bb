from Range import Range
import Instrument
class InstrumentFactory(object):
    def __init__(self):
        self.iattack = Range(0.001,0.05)
        self.idur = Range(0.1,.5)
        self.ipan = Range(0,1,False)
        self.ifreq1 = Range(20,2000)
        self.ifreq2 = Range(20,2000)
        self.ihness = Range(0,.2,False)
        self.idist  = Range(0.25,.50)
    def makeInstrument(self):
        instr = Instrument.Instrument()
        instr.idur =   self.idur()
        instr.iattack =   self.iattack()
        instr.ipan = self.ipan()
        instr.ifreq1 = self.ifreq1()
        instr.ifreq2 = self.ifreq2()
        instr.ihness = self.ihness()
        instr.idist  = self.idist()
        return instr
