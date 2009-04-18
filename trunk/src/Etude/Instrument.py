from InstrumentFactory import InstrumentFactory
from Note import Note
class Instrument(InstrumentFactory):
    def __init__(self):
        super(Instrument,self).__init__()
        self.idur = .5
    def makeNote(self,istart):
        note = Note(istart)
        return note




