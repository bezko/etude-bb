import random
class Sequence():
    def __init__(self,duration,length):
        self.duration = duration
        self.length = length
        self.beats = [0 for i in range(1,length)]
        
    def fill(self,density):
        
       for i in  range(1, self.length):
           if (random.random()<density):               
               self.beats[i-1] = 1
           else:
              self.beats[i-1] = 0
       