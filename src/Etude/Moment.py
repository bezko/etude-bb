from MomentFactory import MomentFactory
class Moment(MomentFactory):
    def __init__(self,start,duration):
        self.start=start
        self.duration =duration