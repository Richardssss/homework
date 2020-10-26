from math import *
import numpy as np
import matplotlib.pyplot as plt
from dW import *

start = float(input("开始值："))
stop = float(input("结束值："))
num = int(input("离散数："))
x = np.linspace(start,stop,num)
y = np.sin(x)
dx = (stop-start) / (num-1)
h = dx * 10.5

dimension = int(input("维度(1,2,3)："))
if dimension == 1:
    ad = 5/(4*h)
elif dimension == 2:
    ad = 5/(pi * h**2)
elif dimension == 3:
    ad = 105 / (16 * pi * h**3)

dY = []

for i in range(num):
    dy = 0
    for j in range(num):
        R = (x[i]-x[j])/h
        dy = sin(x[j]) * dW(R,h,ad) * dx + dy
    dY.append(dy)

plt.plot(x,y,color="blue")
plt.plot(x,np.array(dY),color="red")

plt.show()
