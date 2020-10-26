import math as m

def W(R,h,ad):
    R = abs(R)
    if R<=1:
        y = ad * (1+3*R) * (1-R)**3
    else:
        y=0
    return y