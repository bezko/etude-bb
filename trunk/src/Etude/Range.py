from Utils import exprand,linrand
class Interval():
    def __init__(self,minv,maxv,isexp=True):
        self.minv = minv
        self.maxv = maxv
        self.isexp = isexp
    def __call__(self):
        if self.isexp:
            return exprand(self.minv,self.maxv)
        else:
            return linrand(self.minv,self.maxv)
        