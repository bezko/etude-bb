sr=44100
kr=44100
ksmps=1
nchnls=2

instr 1
	ipan = p4
	
	aenv expseg 1,p3,1/10000
	anoise randh 16000,4000
	
	asound = anoise*aenv

	outs asound*ipan,asound*(1-ipan)
endin