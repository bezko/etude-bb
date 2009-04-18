import random
from Utils import exprand
class Score():
    def __init__(self,dur,mf,filename="etude.sco"):
        self.dur = dur
        self.mf =mf
        istart = 0
        sco = open(filename,"w")
        sco.write("f 1 0 8192 10 1\n")
        while istart<dur:
            m = mf.makeMoment(istart)
            sco.write(m.sco)
            istart += m.duration



