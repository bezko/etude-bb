import Note
import InstrumentFactory
class Instrument(InstrumentFactory.InstrumentFactory):
    def __init__(self):
        super(Instrument,self).__init__()
    def makeNote(self,istart):
        note = Note.Note(istart)
        note.idur =   self.idur
        note.iattack =   self.iattack
        note.ipan = self.ipan
        note.ifreq1 = self.ifreq1
        note.ifreq2 = self.ifreq2
        note.ihness = self.ihness
        note.idist  = self.idist
        return note




