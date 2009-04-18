import os
from Etude import *

#sco = Score()
#os.system("csound -d   -m 4 -W  -o etude.wav etude.orc etude.sco -")
#os.system("aplay etude.wav")

f = InstrumentFactory()
i = f.makeInstrument()
n = f.makeNote(0.666)
print n
