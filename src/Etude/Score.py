import random
from Utils import exprand
class Score():
    def __init__(self,filename="etude.sco"):
        sco = open(filename,"w")
        sco.write("f 1 0 8192 10 1\n")
        for i  in range (1,1000):
            if random.random()>.7 :                
                sco.write("i  1  %f .2  %f .001  %f %f %f 1\n"%((i-1)/10.00, .6,exprand(850,1400),exprand(1000,2250),random.random()))
        for i  in range (1,600):
            if random.random()>.7 :                
                sco.write("i  1  %f .5  .5 .01  %f %f %f 1 \n"%((i-1)/6.0,exprand(50,160),exprand(30,140),random.random())) 
        for i  in range (1,1280):
            if random.random()>.7 :                
                sco.write("i  1  %f .3  %f .001  %f %f %f 1 \n"%((i-1)/12.8, .8,exprand(2250,5260),exprand(11950,17000),random.random()))        
        for i  in range (1,1280):
            if random.random()>.7 :                
                sco.write("i  1  %f .2  %f .001  %f %f %f  .1\n"%((i-1)/12.8,.3,exprand(10250,15260),exprand(10950,18000),random.random()))        
                          