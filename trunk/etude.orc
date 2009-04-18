
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
	idist  = p9
	iseed  = p10


	aenv expseg 0.0001,iattack,1,idur-iattack,0.0001
	arandi_r randi 1,ifreq1,iseed
	arandi_l randi 1,ifreq1,1-iseed

	arandh_r randh 1,ifreq1,iseed
	arandh_l randh 1,ifreq1,1-iseed


	anoise_r = arandi_r*(1-ihness) + ihness*arandh_r
	anoise_l = arandi_l*(1-ihness) + ihness*arandh_l




	amod oscili 1,ifreq2,1,iseed

	astuff_r tablei idist*(anoise_r*aenv*amod)/.5,1,1,.5,1
	astuff_l tablei idist*(anoise_l*aenv*amod)/.5,1,.5,1

	asound_r = astuff_r*2000
	asound_l = astuff_l*2000
	outs asound_r*ipan,asound_l*(1-ipan)
endin