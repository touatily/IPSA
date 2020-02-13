from math import *

def EquiRectDist(la1,lo1,la2,lo2):
    R=6371
    x=(lo2-lo1)*cos((la1+la2)/2)
    y=(la2-la1)
    d=sqrt(x**2+y**2)*R
    return d

def EquiRectDistDeg(la1d,lo1d,la2d,lo2d):
    return EquiRectDist(radians(la1d),radians(lo1d),radians(la2d),radians(lo2d))

