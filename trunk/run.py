import os
from Etude import Sequence
os.system("csound -d  -W  -o etude.wav etude.orc etude.sco -")
os.system("aplay etude.wav")

s = Sequence.Sequence(.1,12)
s.fill(.5)
print s.beats