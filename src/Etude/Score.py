import random
class Score():
    def __init__(self,filename="etude.sco"):
        sco = open(filename,"w")
        sco.write("f 1 0 8192 10 1\n")
        for i  in range (1,1000):
            if random.random()>.6 :                
                sco.write("i  1  %f .2  %f .001  %f %f %f \n"%((i-1)/10.0, random.random(),random.uniform(1150,1200),random.uniform(1200,1250),random.random()))
        for i  in range (1,600):
            if random.random()>.2 :                
                sco.write("i  1  %f .5  .5 .01  %f %f %f \n"%((i-1)/6.0,random.uniform(50,60),random.uniform(30,40),random.random())) 
        for i  in range (1,1280):
            if random.random()>.8 :                
                sco.write("i  1  %f 1  %f .001  %f %f %f \n"%((i-1)/12.8, random.random(),random.uniform(5250,5260),random.uniform(13950,14000),random.random()))        
                 