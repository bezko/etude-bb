
from .Range import Range
class MomentFactory(object):
    def __init__(self,mintime,maxtime):
        self.timerange = Range(mintime,maxtime)
    def makeMoment(self,start):
        from .Moment import Moment
        m = Moment(start,self.timerange())
        return m

