from random import *
from . import Sequence
from .Utils import exprandint
class Phrase(object):
    def __init__(self,f,start,dur,bars):

        self.instr = f.makeInstrument()
        self.sco = ""
        sig = choice([4,8,12,16])
        seq = Sequence(sig)
        bardur = dur/bars
        notedur = bardur/sig
        for b in range(bars+1):
            for t in range(len(seq.beats)):
                if seq.beats[t] == 1:
                    istart = start + b*bardur + t*notedur
                    n = self.instr.makeNote(istart)
                    self.sco += str(n)
            seq.mutate(1)
