import math as m

def dW(R,h,ad):
    if abs(R)<=1:
        if R==0:
            k=0
        else:
            k=R/abs(R)
        R = abs(R)
        y = ad * (1-R)**2 * (-12*R) * k * (1/h)
    else:
        y=0
    return y
