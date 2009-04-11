sr=44100
kr=44100
ksmps=1
nchnls=2

instr 1
	ipan = p4
	
	aenv expseg 0.001,0.01,1,p3-.01,1/10000
	anoise randh 32000,300
	amod oscili 1,1000,1
	
	asound = anoise*aenv*amod

	outs asound*ipan,asound*(1-ipan)
endin

instr 2
	ipan = p4
	
	aenv expseg 0.0001,0.05,1,p3-.01,1/10000
	anoise randi 1,125
	amod oscili 1,50,1
	
	
	astuff tablei (anoise*aenv*amod)*2,1,1,.5,1 
	asound = astuff*16000
	outs asound*ipan,asound*(1-ipan)
endin