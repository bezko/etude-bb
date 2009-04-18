import random

linrand = random.uniform
def exprand (minv,maxv):
    return minv * (maxv/float(minv))**random.random()
def exprandint (minv,maxv):
    return  int( round(exprand (minv,maxv)))
