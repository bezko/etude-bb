import random
class Sequence():
    def __init__(self,length):
        self.length = length
        self.beats = [0 for i in range(1,length)]

    def fill(self,density):

       for i in  range(1, self.length):
           if (random.random()<density):
               self.beats[i-1] = 1
           else:
              self.beats[i-1] = 0
    def mutate(self,n):
        for i in range(n):
            index = random.randint(0,len(self.beats)-1)
            if self.beats[index] == 0:
                self.beats[index] = 1
            else:
                self.beats[index] = 0

