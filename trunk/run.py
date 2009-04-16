import os
from Etude import *

#sco = Score()
os.system("csound -d   -m 4 -W  -o etude.wav etude.orc etude.sco -")
os.system("aplay etude.wav")

#n = Note(.4)
#print n
