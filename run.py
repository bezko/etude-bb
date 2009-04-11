import os
os.system("csound -d  -W  -o etude.wav etude.orc etude.sco -")
os.system("aplay etude.wav")
