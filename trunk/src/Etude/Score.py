import random
from Utils import exprand
class Score():
    def __init__(self,filename="etude.sco"):
        sco = open(filename,"w")
        sco.write("f 1 0 8192 10 1\n")
        for i  in range (1,100):
            if random.random()>.9 :
                sco.write("i  1  %f .2  %f .001  %f %f %f .1 %f\n"%((i-1)/10.00, .6,exprand(1350,1400),exprand(2200,2250),random.random(),random.random()))
        for i  in range (1,60):
            if random.random()>.9 :
                sco.write("i  1  %f .5  .5 .005  %f %f %f 1 %f\n"%((i-1)/6.0,exprand(80,80),exprand(50,50),random.random()/8,random.random()))
        for i  in range (1,128):
            if random.random()>.9 :
                sco.write("i  1  %f .3  %f .001  %f %f %f .5 %f \n"%((i-1)/12.8, .8,exprand(5250,5260),exprand(16950,17000),random.random(),random.random()))
        for i  in range (1,128):
            if random.random()>.9 :
                sco.write("i  1  %f .3  %f .001  %f %f %f  .1 %f\n"%((i-1)/12.8,.3,exprand(10250,10260),exprand(10950,18000),random.random(),random.random()))