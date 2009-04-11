sr=44100
kr=44100
ksmps=1
nchnls=2


instr 1
	idur = p3	
	ipan   = p4
	iattack =p5
	ifreq1 = p6
	ifreq2 = p7
	ihness = p8
	
	 
	
	aenv expseg 0.0001,iattack,1,idur-iattack,0.0001
	anoise_r randi 1,ifreq1,.5
	anoise_l randi 1,ifreq1,.7
	
	
	
	
	amod oscili 1,ifreq2,1,.25
		
	astuff_r tablei (anoise_r*aenv*amod),1,1,.5,1
	astuff_l tablei (anoise_l*aenv*amod),1,1,.5,1
	
	 
	asound_r = astuff_r*16000
	asound_l = astuff_l*16000
	outs asound_r*ipan,asound_l*(1-ipan)
endin