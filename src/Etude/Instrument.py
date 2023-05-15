
from .InstrumentFactory import InstrumentFactory
from .Moment import Moment
class Instrument(InstrumentFactory):
    def __init__(self):
        super(Instrument,self).__init__()
    def makeNote(self,istart):
        from .Note import Note
        note = Note(istart)
        note.idur =   self.idur
        note.iattack =   self.iattack
        note.ipan = self.ipan
        note.ifreq1 = self.ifreq1
        note.ifreq2 = self.ifreq2
        note.ihness = self.ihness
        note.idist  = self.idist
        return note




