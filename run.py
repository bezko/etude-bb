import os, sys
sys.path.append(os.path.join(os.getcwd(), "src"))

from Etude import *

mf = MomentFactory(1,32)


sco = Score(360,mf)
os.system("csound -d   -m 4 -W  -o etude.wav etude.orc etude.sco -")
os.system("aplay etude.wav")

#f = InstrumentFactory()
#i = f.makeInstrument()
#n = i.makeNote(0.666)
#print n
