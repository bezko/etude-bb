from InstrumentFactory import InstrumentFactory
class Instrument(InstrumentFactory):
    def __init__(self):
        super(Instrumnent,self).__init__()
        
        self.idur =.01
        self.ipan =0.5
        self.iattack = 0.01
        self.ifreq1 = 100
        self.ifreq2 = 200
        self.ihness = 01
        self.idist  = .25
        
        
